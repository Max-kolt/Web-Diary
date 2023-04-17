from datetime import datetime

from django.db import models
from django.urls import reverse


class Students(models.Model):
    fname = models.CharField(max_length=50, verbose_name='Имя')
    lname = models.CharField(max_length=50, verbose_name='Фамилия')
    mname = models.CharField(max_length=50, verbose_name='Отчество')
    group = models.ForeignKey('Groups', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fname}  {self.lname}'

    def get_absolute_url(self):
        return reverse('student', kwargs={'stud_id': self.pk})


class Groups(models.Model):
    number = models.IntegerField(verbose_name='Группа')
    specialization = models.ForeignKey('Specializations', on_delete=models.PROTECT, verbose_name='Специализация')

    def __str__(self):
        return f'{self.number}'

    def get_absolute_url(self):
        return reverse('subjects', kwargs={'group_id': self.pk})


class Specializations(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    number = models.CharField(max_length=12, verbose_name='Номер')

    def __str__(self):
        return self.name


class SubjectLessons(models.Model):
    subject_ID = models.ForeignKey('GroupSubjects', on_delete=models.CASCADE, verbose_name='Предмет')
    date = models.DateField(verbose_name='Дата', default=datetime.now())
    topic = models.CharField(max_length=255, null=True, verbose_name='Тема')

    def __str__(self):
        return f'{self.date}'

    class Meta:
        unique_together = ('subject_ID', 'date')


class StudentEstimates(models.Model):
    MARKS = [
        ('1', 'Poor'),
        ('2', 'Unsatisfactory'),
        ('3', 'Satisfactory'),
        ('4', 'Good'),
        ('5', 'Excellent'),
        ('n', 'Absent')
    ]

    student_ID = models.ForeignKey('Students', on_delete=models.CASCADE)
    lesson_ID = models.ForeignKey('SubjectLessons', on_delete=models.CASCADE)
    mark = models.CharField(max_length=1, choices=MARKS)

    def __str__(self):
        return f'({self.lesson_ID}) {self.student_ID}  : {self.mark} '


class Subjects(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    MDK = models.CharField(max_length=6, null=True, verbose_name='МДК')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('subjects', kwargs={'subj_slug': self.slug})


class GroupSubjects(models.Model):
    subject_ID = models.ForeignKey('Subjects', on_delete=models.PROTECT, verbose_name='Предмет')
    group = models.ForeignKey('Groups', on_delete=models.CASCADE, verbose_name='Группа')
    teacher = models.ForeignKey('Teachers', null=True, on_delete=models.SET_NULL, verbose_name='Преподаватель')
    hours = models.IntegerField(verbose_name='Часы')

    def __str__(self):
        return f'{self.group} {self.subject_ID}'


class Teachers(models.Model):
    fname = models.CharField(max_length=50, verbose_name='Имя')
    lname = models.CharField(max_length=50, verbose_name='Фамилия')
    mname = models.CharField(max_length=50, verbose_name='Отчество')

    def __str__(self):
        return f'{self.fname} {self.lname}'

    def get_absolute_url(self):
        return reverse('teacher', kwargs={'teach_id': self.pk})


class StudyEvents(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    photos = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'event_id': self.pk})


class EventResults(models.Model):
    event_ID = models.ForeignKey('StudyEvents', on_delete=models.CASCADE)
    student_ID = models.ForeignKey('Students', null=True, on_delete=models.SET_NULL, verbose_name='Студент')
    result = models.CharField(max_length=255, verbose_name='Достижение')

    def __str__(self):
        return f'{self.student_ID} {self.event_ID} {self.result}'

