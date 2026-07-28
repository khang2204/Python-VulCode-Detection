def mark_changed_translation(changed_entities, locale):...
"""docstring"""
changed_entities_array = []
existing = ChangedEntityLocale.objects.values_list('entity', 'locale'
    ).distinct()
for changed_entity in changed_entities:
key = changed_entity.pk, locale.pk
ChangedEntityLocale.objects.bulk_create(changed_entities_array)
if key not in existing:
changed_entities_array.append(ChangedEntityLocale(entity=changed_entity,
    locale=locale))
