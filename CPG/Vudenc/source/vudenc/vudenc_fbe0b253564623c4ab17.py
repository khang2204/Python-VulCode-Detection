def save(self, *args, **kwargs):...
editor_ip = self.cleaned_data['user_ip']
comment = self.cleaned_data['comment']
article = super(ArticleForm, self).save(*args, **kwargs)
editor = getattr(self, 'editor', None)
group = getattr(self, 'group', None)
if self.is_new:
article.creator_ip = editor_ip
changeset = article.new_revision(self.old_content, self.old_title, self.
    old_markup, comment, editor_ip, editor)
if editor is not None:
return article, changeset
article.creator = editor
article.save(*args, **kwargs)
article.group = group
