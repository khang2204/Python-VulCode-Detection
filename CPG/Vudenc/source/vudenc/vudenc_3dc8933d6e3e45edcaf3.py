def get_context_data(self, **kwargs):...
context = super().get_context_data(**kwargs)
context['articles'] = self.object.article_set.all()
context['form'] = CommentForm()
return context
