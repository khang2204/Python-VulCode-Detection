def validate_unique_project_path(project: Project, path: str,...
"""docstring"""
existing_sources = FileSource.objects.filter(project=project, path=path)
if existing_source_pk:
existing_sources = existing_sources.exclude(pk=existing_source_pk)
if len(existing_sources):
