"""
RESTful URL patterns and routing for the Deis API app.


Applications
============

.. http:get:: /api/apps/(string:id)/

  Retrieve a :class:`~api.models.App` by its `id`.

.. http:delete:: /api/apps/(string:id)/

  Destroy a :class:`~api.models.App` by its `id`.

.. http:get:: /api/apps/

  List all :class:`~api.models.App`\\s.

.. http:post:: /api/apps/

  Create a new :class:`~api.models.App`.


Application Release Components
------------------------------

.. http:get:: /api/apps/(string:id)/config/

  List all :class:`~api.models.Config`\\s.

.. http:post:: /api/apps/(string:id)/config/

  Create a new :class:`~api.models.Config`.

.. http:get:: /api/apps/(string:id)/builds/(string:uuid)/

  Retrieve a :class:`~api.models.Build` by its `uuid`.

.. http:get:: /api/apps/(string:id)/builds/

  List all :class:`~api.models.Build`\\s.

.. http:post:: /api/apps/(string:id)/builds/

  Create a new :class:`~api.models.Build`.

.. http:get:: /api/apps/(string:id)/releases/(int:version)/

  Retrieve a :class:`~api.models.Release` by its `version`.

.. http:get:: /api/apps/(string:id)/releases/

  List all :class:`~api.models.Release`\\s.

.. http:post:: /api/apps/(string:id)/releases/rollback/

  Rollback to a previous :class:`~api.models.Release`.


Application Infrastructure
--------------------------

.. http:get:: /api/apps/(string:id)/containers/(string:type)/(int:num)/

  List all :class:`~api.models.Container`\\s.

.. http:get:: /api/apps/(string:id)/containers/(string:type)/

  List all :class:`~api.models.Container`\\s.

.. http:get:: /api/apps/(string:id)/containers/

  List all :class:`~api.models.Container`\\s.


Application Domains
-------------------


.. http:delete:: /api/apps/(string:id)/domains/(string:hostname)

  Destroy a :class:`~api.models.Domain` by its `hostname`

.. http:get:: /api/apps/(string:id)/domains/

  List all :class:`~api.models.Domain`\\s.

.. http:post:: /api/apps/(string:id)/domains/

  Create a new :class:`~api.models.Domain`\\s.


Application Actions
-------------------

.. http:post:: /api/apps/(string:id)/scale/

  See also
  :meth:`AppViewSet.scale() <api.views.AppViewSet.scale>`

.. http:get:: /api/apps/(string:id)/logs/

  See also
  :meth:`AppViewSet.logs() <api.views.AppViewSet.logs>`

.. http:post:: /api/apps/(string:id)/run/

  See also
  :meth:`AppViewSet.run() <api.views.AppViewSet.run>`


Application Sharing
===================

.. http:delete:: /api/apps/(string:id)/perms/(string:username)/

  Destroy an app permission by its `username`.

.. http:get:: /api/apps/(string:id)/perms/

  List all permissions granted to this app.

.. http:post:: /api/apps/(string:id)/perms/

  Create a new app permission.


Keys
====

.. http:get:: /api/keys/(string:id)/

  Retrieve a :class:`~api.models.Key` by its `id`.

.. http:delete:: /api/keys/(string:id)/

  Destroy a :class:`~api.models.Key` by its `id`.

.. http:get:: /api/keys/

  List all :class:`~api.models.Key`\\s.

.. http:post:: /api/keys/

  Create a new :class:`~api.models.Key`.


API Hooks
=========

.. http:post:: /api/hooks/push/

  Create a new :class:`~api.models.Push`.

.. http:post:: /api/hooks/build/

  Create a new :class:`~api.models.Build`.

.. http:post:: /api/hooks/config/

  Retrieve latest application :class:`~api.models.Config`.


Auth
====

.. http:post:: /api/auth/register/

  Create a new User.

.. http:delete:: /api/auth/register/

  Destroy the logged-in User.

.. http:post:: /api/auth/login

  Authenticate for the REST framework.

.. http:post:: /api/auth/logout

  Clear authentication for the REST framework.

.. http:get:: /api/generate-api-key/

  Generate an API key.


Admin Sharing
=============

.. http:delete:: /api/admin/perms/(string:username)/

  Destroy an admin permission by its `username`.

.. http:get:: /api/admin/perms/

  List all admin permissions granted.

.. http:post:: /api/admin/perms/

  Create a new admin permission.

"""
from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from api import routers
from api import views
router = routers.ApiRouter()
urlpatterns = patterns('', url('^', include(router.urls)), url(
    '^apps/(?P<id>{})/config/?'.format(settings.APP_URL_REGEX), views.
    AppConfigViewSet.as_view({'get': 'retrieve', 'post': 'create'})), url(
    '^apps/(?P<id>{})/builds/(?P<uuid>[-_\\w]+)/?'.format(settings.
    APP_URL_REGEX), views.AppBuildViewSet.as_view({'get': 'retrieve'})),
    url('^apps/(?P<id>{})/builds/?'.format(settings.APP_URL_REGEX), views.
    AppBuildViewSet.as_view({'get': 'list', 'post': 'create'})), url(
    '^apps/(?P<id>{})/releases/v(?P<version>[0-9]+)/?'.format(settings.
    APP_URL_REGEX), views.AppReleaseViewSet.as_view({'get': 'retrieve'})),
    url('^apps/(?P<id>{})/releases/rollback/?'.format(settings.
    APP_URL_REGEX), views.AppReleaseViewSet.as_view({'post': 'rollback'})),
    url('^apps/(?P<id>{})/releases/?'.format(settings.APP_URL_REGEX), views
    .AppReleaseViewSet.as_view({'get': 'list'})), url(
    '^apps/(?P<id>{})/containers/(?P<type>[-_\\w]+)/(?P<num>[-_\\w]+)/?'.
    format(settings.APP_URL_REGEX), views.AppContainerViewSet.as_view({
    'get': 'retrieve'})), url(
    '^apps/(?P<id>{})/containers/(?P<type>[-_\\w.]+)/?'.format(settings.
    APP_URL_REGEX), views.AppContainerViewSet.as_view({'get': 'list'})),
    url('^apps/(?P<id>{})/containers/?'.format(settings.APP_URL_REGEX),
    views.AppContainerViewSet.as_view({'get': 'list'})), url(
    '^apps/(?P<id>{})/domains/(?P<domain>[-\\._\\w]+)/?'.format(settings.
    APP_URL_REGEX), views.DomainViewSet.as_view({'delete': 'destroy'})),
    url('^apps/(?P<id>{})/domains/?'.format(settings.APP_URL_REGEX), views.
    DomainViewSet.as_view({'post': 'create', 'get': 'list'})), url(
    '^apps/(?P<id>{})/scale/?'.format(settings.APP_URL_REGEX), views.
    AppViewSet.as_view({'post': 'scale'})), url('^apps/(?P<id>{})/logs/?'.
    format(settings.APP_URL_REGEX), views.AppViewSet.as_view({'get': 'logs'
    })), url('^apps/(?P<id>{})/run/?'.format(settings.APP_URL_REGEX), views
    .AppViewSet.as_view({'post': 'run'})), url(
    '^apps/(?P<id>{})/perms/(?P<username>[-_\\w]+)/?'.format(settings.
    APP_URL_REGEX), views.AppPermsViewSet.as_view({'delete': 'destroy'})),
    url('^apps/(?P<id>{})/perms/?'.format(settings.APP_URL_REGEX), views.
    AppPermsViewSet.as_view({'get': 'list', 'post': 'create'})), url(
    '^apps/(?P<id>{})/?'.format(settings.APP_URL_REGEX), views.AppViewSet.
    as_view({'get': 'retrieve', 'delete': 'destroy'})), url('^apps/?',
    views.AppViewSet.as_view({'get': 'list', 'post': 'create'})), url(
    '^keys/(?P<id>.+)/?', views.KeyViewSet.as_view({'get': 'retrieve',
    'delete': 'destroy'})), url('^keys/?', views.KeyViewSet.as_view({'get':
    'list', 'post': 'create'})), url('^hooks/push/?', views.PushHookViewSet
    .as_view({'post': 'create'})), url('^hooks/build/?', views.
    BuildHookViewSet.as_view({'post': 'create'})), url('^hooks/config/?',
    views.ConfigHookViewSet.as_view({'post': 'create'})), url(
    '^auth/register/?', views.UserRegistrationView.as_view({'post':
    'create'})), url('^auth/cancel/?', views.UserCancellationView.as_view({
    'delete': 'destroy'})), url('^auth/', include('rest_framework.urls',
    namespace='rest_framework')), url('^generate-api-key/',
    'rest_framework.authtoken.views.obtain_auth_token'), url(
    '^admin/perms/(?P<username>[-_\\w]+)/?', views.AdminPermsViewSet.
    as_view({'delete': 'destroy'})), url('^admin/perms/?', views.
    AdminPermsViewSet.as_view({'get': 'list', 'post': 'create'})))
