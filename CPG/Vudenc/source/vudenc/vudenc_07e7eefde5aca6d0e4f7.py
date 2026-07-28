import os
import csv
import zipfile
from itertools import islice
from collections import OrderedDict
from djqscsv import render_to_csv_response
from pathlib import Path
from django import forms
from django.urls import reverse
from django.conf import settings
from django.core.files import File
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from dashboard.models import *
from dashboard.forms import DataGroupForm, ExtractionScriptForm, CleanCompDataForm, create_detail_formset, include_extract_form, include_clean_comp_data_form
from dashboard.utils import get_extracted_models, clean_dict, update_fields
from django.db.models import Max
@login_required()...
datagroup = DataGroup.objects.all()
data = {}
data['object_list'] = datagroup
return render(request, template_name, data)
