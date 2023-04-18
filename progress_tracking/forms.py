from django import forms
from .models import *


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['fname', 'lname', 'mname', 'group']


class LessonsForm(forms.ModelForm):
    class Meta:
        model = SubjectLessons
        fields = ['topic']


class GroupsForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['number', 'specialization']
        widgets = { 'specialization': forms.Select(attrs={'style': 'width: 100%'}) }


class TeachersForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ['fname', 'lname', 'mname']


class EventsForm(forms.ModelForm):
    class Meta:
        model = StudyEvents
        fields = ['name', 'description', 'photos']
