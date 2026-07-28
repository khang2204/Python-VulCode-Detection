"""

View partials provide all the callisto-core front-end functionality.
Subclass these partials with your own views if you are implementing
callisto-core. Many of the view partials only provide a subset of the
functionality required for a full HTML view.

docs / reference:
    - https://docs.djangoproject.com/en/1.11/topics/class-based-views/
    - https://github.com/project-callisto/callisto-core/blob/master/callisto_core/wizard_builder/view_partials.py

view_partials should define:
    - forms
    - models
    - helper classes
    - access checks
    - redirect handlers

and should not define:
    - templates
    - url names

"""
import logging
import re
import ratelimit.mixins
from nacl.exceptions import CryptoError
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from callisto_core.evaluation.view_partials import EvalDataMixin
from callisto_core.reporting import report_delivery
from callisto_core.wizard_builder import data_helper, view_partials as wizard_builder_partials
from . import forms, models, view_helpers
logger = logging.getLogger(__name__)
storage_helper = view_helpers.ReportStorageHelper
@property...
return self.storage_helper(self)
