def get_context_data(self):...
data = super().get_context_data()
data['life_conditions'] = LifeCondition.objects.with_benefits()
return data
