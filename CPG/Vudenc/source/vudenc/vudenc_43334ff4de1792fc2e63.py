def simics_register_diff_choices(self, attribute):...
choices = []
for item in self.queryset.filter(result__campaign_id=self.campaign
choices.append((item, item))
return sorted(choices, key=fix_sort_list)
