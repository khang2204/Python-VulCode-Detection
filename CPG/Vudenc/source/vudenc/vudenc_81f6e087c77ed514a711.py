"""URL routing module."""
from django.conf import urls
import site_settings
import views.admin.statistics
_BASE_URL_PATTERNS = [('global/admin/statistics/?', views.admin.statistics.
    AdminStatisticsView.as_view)]
urlpatterns = [urls.url('^(%s)$' % path_exp, view_func()) for path_exp,
    view_func in _BASE_URL_PATTERNS]
if site_settings.OPTIONAL_PATH_PREFIX:
urlpatterns += [urls.url('^(%s)/(%s)$' % (site_settings.
    OPTIONAL_PATH_PREFIX, path_exp), view_func()) for path_exp, view_func in
    _BASE_URL_PATTERNS]
