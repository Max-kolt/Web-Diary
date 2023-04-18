from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('groups/', show_groups, name='groups'),
    path('<int:group_id>/', show_group_subjects, name='subjects'),
    path('<int:group_id>/<slug:subj_slug>', show_group_estimates, name='estimates'),
    path('<int:group_id>/<slug:subj_slug>/save', save_estmimates, name='save_estmimates'),
    path('<int:group_id>/new_stud', new_student, name='new_stud'),

    #path('', ),
    path('logout/', logout, name='logout'),

    path('events/', events, name='events'),
    path('event/<int:event_id>', current_event, name='event')
]

