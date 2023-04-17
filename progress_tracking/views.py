import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from .models import *
from .forms import *

main_menu = [
    {'title': 'Dairy', 'url_path': 'groups'},
    {'title': 'Events', 'url_path': 'events'}
]


def home(request):
    groups = Groups.objects.order_by('-pk')[0:5]
    events = StudyEvents.objects.order_by('-pk')[0:5]
    return render(
        request,
        'index.html',
        {
            'content': 'Главная страница',
            'menu': main_menu,
            'groups': groups,
            'events': events,
        }
    )


def show_groups(request):
    all_groups = Groups.objects.all()
    context = {
        'menu': main_menu,
        'title': 'Выберите группу',
        'groups': all_groups
    }

    return render(
        request,
        'progress_tracking/groups.html',
        context=context
    )


def show_group_subjects(request, group_id):
    group_subjects = GroupSubjects.objects.filter(group=group_id)

    context = {
        'menu': main_menu,
        'title': 'Выберите предмет',
        'subjects': group_subjects,
        'group_id': group_id
    }
    return render(
        request,
        'progress_tracking/subjects.html',
        context=context
    )


def show_group_estimates(request, group_id, subj_slug):
    students = Students.objects.filter(group=group_id)
    subj = Subjects.objects.get(slug=subj_slug)
    subject_for_group = GroupSubjects.objects.get(subject_ID=subj.id)

    if request.method == 'POST':
        print(request.POST)
        form = LessonsForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.subject_ID = subject_for_group
            lesson.save()
            return redirect(f'/{group_id}/{subj_slug}')
    else:
        form = LessonsForm()

    lessons = SubjectLessons.objects.filter(subject_ID=subject_for_group.pk)

    table_matrix = []
    for stud in students:
        current_student = {'stud_name': f'{stud.lname} {stud.fname} {stud.mname}', 'stud_id': stud.pk, 'estimates': []}
        for lesson in lessons:
            stud_lesson = StudentEstimates.objects.filter(lesson_ID=lesson.pk)
            try:
                stud_mark = stud_lesson.get(student_ID=stud.pk)
                current_student['estimates'].append({'date': lesson.date, 'mark': stud_mark.mark})
            except Exception:
                current_student['estimates'].append({'date': lesson.date, 'mark': None})
        table_matrix.append(current_student)

    context = {
        'menu': main_menu,
        'title': f'{subj.name}',
        'lessons': lessons,
        'estimate_matrix': table_matrix,
        'group_id': group_id,
        'subj_slug': subj_slug,
        'form': form
    }
    return render(
        request,
        'progress_tracking/table.html',
        context=context
    )


def save_estmimates(request, group_id, subj_slug):
    response = {}
    data = json.load(request)
    try:
        remove_data = data.get('removes')
        add_data = data.get('add')
    except Exception:
        remove_data = []
        add_data = []
    subj = Subjects.objects.get(slug=subj_slug)
    group_subj = GroupSubjects.objects.get(group=group_id, subject_ID=subj.pk)

    for i in remove_data:
        lesson = SubjectLessons.objects.get(subject_ID=group_subj.pk, date=i['date'])
        student = Students.objects.get(pk=int(i['stud_id']))
        try:
            stud = StudentEstimates.objects.get(student_ID=student, lesson_ID=lesson)
            stud.delete()
        except Exception:
            pass

    for i in add_data:
        lesson = SubjectLessons.objects.get(subject_ID=group_subj.pk, date=i['date'])
        student = Students.objects.get(pk=int(i['stud_id']))
        try:
            stud = StudentEstimates.objects.get(student_ID=student, lesson_ID=lesson)
            stud.mark = i['mark']
            stud.save()
        except Exception:
            StudentEstimates.objects.create(student_ID=student, lesson_ID=lesson, mark=i['mark'])

    response['is_saved'] = 'Изменения сохранены успешно'

    return JsonResponse(response)


def add_topic_form(request, group_id, subj_slug):
    pass


def events(request):
    events = StudyEvents.objects.all()
    return render(
        request,
        'progress_tracking/events.html',
        {
            'menu': main_menu,
            'events': events
        }
    )


def current_event(request, event_id):
    event = StudyEvents.objects.get(pk=event_id)
    return render(
        request,
        'progress_tracking/current_event.html',
        {
            'menu': main_menu,
            'event': event
        }
    )


@login_required
def logout(request):
    django_logout(request)
    return redirect('home')