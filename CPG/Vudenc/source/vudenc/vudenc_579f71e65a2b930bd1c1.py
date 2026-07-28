from django.db import models
from .common_info import CommonInfo
from django.core.exceptions import ValidationError
from .extracted_text import ExtractedText
from .unit_type import UnitType
from .weight_fraction_type import WeightFractionType
from .raw_chem import RawChem
def validate_ingredient_rank(value):...
if value < 1 or value > 999:
raw_cas_old = models.CharField('Raw CAS', max_length=100, null=True, blank=True
    )
raw_chem_name_old = models.CharField('Raw chemical name', max_length=500,
    null=True, blank=True)
raw_min_comp = models.CharField('Raw minimum composition', max_length=100,
    null=True, blank=True)
raw_max_comp = models.CharField('Raw maximum composition', max_length=100,
    null=True, blank=True)
unit_type = models.ForeignKey(UnitType, on_delete=models.PROTECT)
report_funcuse = models.CharField('Reported functional use', max_length=100,
    null=True, blank=True)
weight_fraction_type = models.ForeignKey(WeightFractionType, on_delete=
    models.PROTECT, null=True, default='1')
ingredient_rank = models.PositiveIntegerField('Ingredient rank', null=True,
    blank=True, validators=[validate_ingredient_rank])
raw_central_comp = models.CharField('Raw central composition', max_length=
    100, null=True, blank=True)
def __str__(self):...
return str(self.raw_chem_name) if self.raw_chem_name else ''
