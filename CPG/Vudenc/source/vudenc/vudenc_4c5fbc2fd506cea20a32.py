def update_stats(translated_resources, locale):...
"""docstring"""
projects = set()
for translated_resource in translated_resources:
projects.add(translated_resource.resource.project)
bulk_update(translated_resources, update_fields=['total_strings',
    'approved_strings', 'fuzzy_strings', 'strings_with_errors',
    'strings_with_warnings', 'unreviewed_strings'])
translated_resource.calculate_stats(save=False)
locale.aggregate_stats()
for project in projects:
project.aggregate_stats()
ProjectLocale.objects.get(locale=locale, project=project).aggregate_stats()
