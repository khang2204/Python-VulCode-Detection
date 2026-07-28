def update_translation_memory(changed_translation_pks, project, locale):...
"""docstring"""
memory_entries = [TranslationMemoryEntry(source=t.entity.string, target=t.
    string, locale=locale, entity=t.entity, translation=t, project=project) for
    t in Translation.objects.filter(pk__in=changed_translation_pks).
    prefetch_related('entity__resource')]
TranslationMemoryEntry.objects.bulk_create(memory_entries)
