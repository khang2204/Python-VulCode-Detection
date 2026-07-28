from django.db import models
from dashboard.models import CommonInfo
from .raw_chem import RawChem
raw_cas_old = models.CharField('Raw CAS', max_length=100, null=True, blank=True
    )
raw_chem_name_old = models.CharField('Raw chemical name', max_length=500,
    null=True, blank=True)
qa_flag = models.BooleanField(default=False)
@classmethod...
return ['raw_cas', 'raw_chem_name']
