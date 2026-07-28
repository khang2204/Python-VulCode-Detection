def form_valid(self, form):...
a = form.save(commit=False)
a.author = self.request.user
a.article = self.object
a.save()
return super().form_valid(form)
