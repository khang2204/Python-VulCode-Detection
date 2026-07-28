"""Django models for the redirects app."""
import logging
import re
from django.db import models
from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _
from readthedocs.core.resolver import resolve_path
from readthedocs.projects.models import Project
from .managers import RedirectManager
log = logging.getLogger(__name__)
HTTP_STATUS_CHOICES = (301, _('301 - Permanent Redirect')), (302, _(
    '302 - Temporary Redirect'))
STATUS_CHOICES = (True, _('Active')), (False, _('Inactive'))
TYPE_CHOICES = ('prefix', _('Prefix Redirect')), ('page', _('Page Redirect')
    ), ('exact', _('Exact Redirect')), ('sphinx_html', _(
    'Sphinx HTMLDir -> HTML')), ('sphinx_htmldir', _('Sphinx HTML -> HTMLDir'))
from_url_helptext = _(
    'Absolute path, excluding the domain. Example: <b>/docs/</b>  or <b>/install.html</b>'
    )
to_url_helptext = _(
    'Absolute or relative URL. Example: <b>/tutorial/install.html</b>')
redirect_type_helptext = _('The type of redirect you wish to use.')
"""A HTTP redirect associated with a Project."""
project = models.ForeignKey(Project, verbose_name=_('Project'),
    related_name='redirects')
redirect_type = models.CharField(_('Redirect Type'), max_length=255,
    choices=TYPE_CHOICES, help_text=redirect_type_helptext)
from_url = models.CharField(_('From URL'), max_length=255, db_index=True,
    help_text=from_url_helptext, blank=True)
to_url = models.CharField(_('To URL'), max_length=255, db_index=True,
    help_text=to_url_helptext, blank=True)
http_status = models.SmallIntegerField(_('HTTP Status'), choices=
    HTTP_STATUS_CHOICES, default=301)
status = models.BooleanField(choices=STATUS_CHOICES, default=True)
create_dt = models.DateTimeField(auto_now_add=True)
update_dt = models.DateTimeField(auto_now=True)
objects = RedirectManager()
verbose_name = _('redirect')
verbose_name_plural = _('redirects')
ordering = '-update_dt',
def __str__(self):...
redirect_text = '{type}: {from_to_url}'
if self.redirect_type in ['prefix', 'page', 'exact']:
return redirect_text.format(type=self.get_redirect_type_display(),
    from_to_url=self.get_from_to_url_display())
return ugettext('Redirect: {}'.format(self.get_redirect_type_display()))
