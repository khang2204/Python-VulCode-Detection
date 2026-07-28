def get_queryset(self):...
action = get_object_or_404(Action, pk=self.kwargs['pk'], published=True)
return self.get_serializer_class().setup_eager_loading(action.actionlog_set
    .all().order_by('-modified'))
