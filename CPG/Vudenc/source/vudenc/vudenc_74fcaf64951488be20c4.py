import os
import shutil
import uuid
from factotum import settings
from pathlib import Path, PurePath
from django.db import models
from .common_info import CommonInfo
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from model_utils import FieldTracker
from django.core.exceptions import ValidationError
from .group_type import GroupType
from .extracted_text import ExtractedText
from .extracted_cpcat import ExtractedCPCat
from .extracted_chemical import ExtractedChemical
from .extracted_functional_use import ExtractedFunctionalUse
from .extracted_list_presence import ExtractedListPresence
def update_filename(instance, filename):...
name_fill_space = instance.name.replace(' ', '_')
name = '{0}/{0}_{1}'.format(name_fill_space, filename)
return name
