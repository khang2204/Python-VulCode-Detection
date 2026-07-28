from django.conf.urls import url, include
from .projects import ProjectViewSet
from .tasks import TaskViewSet, TaskTiles, TaskTilesJson, TaskAssets
from .processingnodes import ProcessingNodeViewSet
from rest_framework_nested import routers
router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('processingnodes', ProcessingNodeViewSet)
tasks_router = routers.NestedSimpleRouter(router, 'projects', lookup='project')
tasks_router.register('tasks', TaskViewSet, base_name='projects-tasks')
urlpatterns = [url('^', include(router.urls)), url('^', include(
    tasks_router.urls)), url(
    'projects/(?P<project_pk>[^/.]+)/tasks/(?P<pk>[^/.]+)/tiles/(?P<z>[\\d]+)/(?P<x>[\\d]+)/(?P<y>[\\d]+)\\.png$'
    , TaskTiles.as_view()), url(
    'projects/(?P<project_pk>[^/.]+)/tasks/(?P<pk>[^/.]+)/tiles\\.json$',
    TaskTilesJson.as_view()), url(
    'projects/(?P<project_pk>[^/.]+)/tasks/(?P<pk>[^/.]+)/download/(?P<asset>[^/.]+)/$'
    , TaskAssets.as_view()), url('^auth/', include('rest_framework.urls'))]
