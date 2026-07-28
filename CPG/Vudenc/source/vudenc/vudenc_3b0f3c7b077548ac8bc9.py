def result_choices(campaign, attribute):...
choices = []
for item in result.objects.filter(campaign_id=campaign).values_list(attribute,
if item is not None:
return sorted(choices, key=fix_sort_list)
choices.append((item, item))
