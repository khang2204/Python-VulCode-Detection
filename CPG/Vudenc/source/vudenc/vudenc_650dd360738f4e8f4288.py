import math
from random import shuffle
from django.db import models
from django.urls import reverse
from django.core.validators import URLValidator, MaxValueValidator, MinValueValidator
from .common_info import CommonInfo
from .data_document import DataDocument
TYPE_CHOICES = ('DL', 'download'), ('EX', 'extraction'), ('PC',
    'product categorization'), ('DC', 'data cleaning')
QA_COMPLETE_PERCENTAGE = 0.2
title = models.CharField(max_length=50)
url = models.CharField(max_length=100, null=True, blank=True, validators=[
    URLValidator()])
qa_begun = models.BooleanField(default=False)
script_type = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=
    False, default='EX')
confidence = models.PositiveSmallIntegerField('Confidence', blank=True,
    validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)
def __str__(self):...
return str(self.title)
