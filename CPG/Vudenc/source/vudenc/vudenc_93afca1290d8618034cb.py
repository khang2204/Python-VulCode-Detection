from django.contrib import admin
from django.urls import re_path
from Shortener_App.views import HomeView, SuccessUrlView, CustomShortURLCreateView, ShortManyURLSView, URLDetailView, URLUpdateView, URLDeleteView, CategoryCreateView, CategoryListView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView, ClickTrackingDetailView, link_redirect
urlpatterns = [re_path('admin/', admin.site.urls), re_path('^$', HomeView.
    as_view(), name='home-view'), re_path('^success/(?P<pk>(\\d)+)/$',
    SuccessUrlView.as_view(), name='success-url-view'), re_path(
    '^add-custom/$', CustomShortURLCreateView.as_view(), name=
    'add-custom-url'), re_path('^add-many/$', ShortManyURLSView.as_view(),
    name='add-many-urls'), re_path('^detail/(?P<pk>(\\d)+)/$',
    URLDetailView.as_view(), name='url-detail-view'), re_path(
    '^update/(?P<pk>(\\d)+)/$', URLUpdateView.as_view(), name=
    'url-update-view'), re_path('^delete/(?P<pk>(\\d)+)/$', URLDeleteView.
    as_view(), name='url-delete-view'), re_path('^category/add/$',
    CategoryCreateView.as_view(), name='category-create-view'), re_path(
    '^categories/$', CategoryListView.as_view(), name='category-list-view'),
    re_path('^detail/category/(?P<pk>(\\d)+)/$', CategoryDetailView.as_view
    (), name='category-detail-view'), re_path(
    '^update/category/(?P<pk>(\\d)+)/$', CategoryUpdateView.as_view(), name
    ='category-update-view'), re_path('^delete/category/(?P<pk>(\\d)+)/$',
    CategoryDeleteView.as_view(), name='category-delete-view'), re_path(
    '^(?P<pk>(\\d)+)/reports/$', ClickTrackingDetailView.as_view(), name=
    'clicktracking-detail-view'), re_path('^(?P<pk>(\\d)+)/$',
    link_redirect, name='url-redirect-view')]
