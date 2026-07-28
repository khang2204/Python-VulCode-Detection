def event_choices(self, campaign, attribute):...
choices = []
for item in event.objects.filter(result__campaign_id=campaign).values_list(
if item is not None:
return sorted(choices, key=fix_sort_list)
choices.append((item, item))
