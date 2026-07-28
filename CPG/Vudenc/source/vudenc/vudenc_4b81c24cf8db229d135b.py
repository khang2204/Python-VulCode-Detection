from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from django.conf.urls import patterns, url
from apps.home.views import home_page, projects, project, project_clone
urlpatterns = patterns('', url('^$', home_page, name='home_page'), url(
    '^draw/?$', home_page, name='home_page'), url('^account/?$', home_page,
    name='account'), url('^projects/$', projects, name='projects'), url(
    '^project/$', project, name='project'), url('^project/new/', project,
    name='project'), url('^project/(?P<proj_id>[0-9]+)/$', project, name=
    'project'), url('^project/(?P<proj_id>[0-9]+)/clone/?$', project_clone,
    name='project_clone'), url(
    '^project/(?P<proj_id>[0-9]+)/scenario/(?P<scenario_id>[0-9]+)/$',
    project, name='project'), url('^project/compare/$', project, name=
    'project'), url('^project/(?P<proj_id>[0-9]+)/compare/$', project, name
    ='project'), url('^analyze$', home_page, name='analyze'), url(
    '^search$', home_page, name='search'), url('^error', home_page, name=
    'error'), url('^sign-up', home_page, name='sign_up'))
