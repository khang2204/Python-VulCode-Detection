from itertools import chain
from datetime import datetime
from model_utils.managers import InheritanceManager
from django.db import models
from django.core.exceptions import ValidationError
from django import forms
from django.urls import reverse
from .common_info import CommonInfo
data_document = models.OneToOneField('DataDocument', on_delete=models.
    CASCADE, primary_key=True)
prod_name = models.CharField(max_length=500, null=True, blank=True)
doc_date = models.CharField(max_length=25, null=True, blank=True)
rev_num = models.CharField(max_length=50, null=True, blank=True)
extraction_script = models.ForeignKey('Script', on_delete=models.CASCADE,
    limit_choices_to={'script_type': 'EX'})
qa_checked = models.BooleanField(default=False, verbose_name='QA approved')
qa_edited = models.BooleanField(default=False, verbose_name='QA edited')
qa_approved_date = models.DateTimeField(null=True, blank=True, verbose_name
    ='QA approval date')
qa_approved_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL,
    verbose_name='QA approved by', null=True, blank=True)
qa_group = models.ForeignKey('QAGroup', verbose_name='QA group', on_delete=
    models.SET_NULL, null=True, blank=True)
objects = InheritanceManager()
def __str__(self):...
return str(self.data_document)
