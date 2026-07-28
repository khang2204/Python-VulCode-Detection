def __str__(self):...
redirect_text = '{type}: {from_to_url}'
if self.redirect_type in ['prefix', 'page', 'exact']:
return redirect_text.format(type=self.get_redirect_type_display(),
    from_to_url=self.get_from_to_url_display())
return ugettext('Redirect: {}'.format(self.get_redirect_type_display()))
