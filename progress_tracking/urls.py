from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('groups/', show_groups, name='groups'),
    path('groups/<int:group_id>/', show_group_subjects, name='subjects'),
    path('groups/<int:group_id>/<slug:subj_slug>', show_group_estimates, name='estimates'),
    path('groups/<int:group_id>/<slug:subj_slug>/save', save_estmimates, name='save_estmimates'),
    path('groups/<int:group_id>/<slug:subj_slug>/add_topic', add_post_form, name='add_post'),
    path('logout/', logout, name='logout'),
    path('events/', events, name='events'),
]


# Разработать техническое задание на программное обеспечивание с учетом изученных стандартов, учебник Гагариной Технологии разработки программного обеспечивания по вариантам