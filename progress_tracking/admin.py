from django.contrib import admin
from .models import *

admin.site.register(Students)
admin.site.register(Specializations)
admin.site.register(StudentEstimates)
admin.site.register(SubjectLessons)
admin.site.register(Subjects)
admin.site.register(Groups)
admin.site.register(GroupSubjects)
admin.site.register(Teachers)
admin.site.register(StudyEvents)
admin.site.register(EventResults)

