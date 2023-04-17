from django import forms
from .models import *


class StudentsForm(forms.Form):
    class Meta:
        model = Students
        fields = ['fname', 'lname', 'mname']


class LessonsForm(forms.ModelForm):
    class Meta:
        model = SubjectLessons
        fields = ['topic']


class GroupsForm(forms.Form):
    class Meta:
        model = Groups
        fields = '__all__'


class TeachersForm(forms.Form):
    class Meta:
        model = Teachers
        fields = '__all__'
