from django.conf.urls import url
from . import views
from .views import ProblemUpdate, ProblemCreate, ProblemDelete


urlpatterns = [
    url(r'^(?P<problem_pk>\d+)/solutions/(?P<user_pk>\d+)$',
        views.problem_solution,
        name='problem_solution'),
    url(r'^(?P<problem_pk>\d+)/download/$',
        views.problem_attempt_file,
        name='problem_attempt_file'),
    url(r'^(?P<problem_pk>\d+)/edit/$',
        views.problem_edit_file,
        name='problem_edit_file'),
    url(r'^(?P<problem_pk>\d+)/move/(?P<shift>-?\d+)/$',
        views.problem_move,
        name='problem_move'),
    url(r'^(?P<problem_pk>\d+)/move_to/',
        views.move_to_form,
        name='problem_move_to'),
    url(r'^(?P<pk>\d+)/update/$',
        ProblemUpdate.as_view(),
        name='problem_update'),
    url(r'^create/(?P<problem_set_id>\d+)/$',
        ProblemCreate.as_view(),
        name='problem_create'),
    url(r'^(?P<pk>\d+)/delete/',
        ProblemDelete.as_view(),
        name='problem_delete'),
    url(r'^(?P<problem_pk>\d+)/copy/',
        views.copy_form,
        name='problem_copy'),
]
