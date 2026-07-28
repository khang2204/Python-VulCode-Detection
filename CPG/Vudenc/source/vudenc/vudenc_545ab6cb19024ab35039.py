from django.views.generic import TemplateView, FormView, DetailView
from django.urls import reverse
from .entryform import EntryForm, entry_form_config, build_question_flag
from .models import LifeCondition, Benefit, BenefitRequirement
template_name = 'core/benefit_overview.html'
def get_context_data(self):...
data = super().get_context_data()
data['life_conditions'] = LifeCondition.objects.with_benefits()
return data
