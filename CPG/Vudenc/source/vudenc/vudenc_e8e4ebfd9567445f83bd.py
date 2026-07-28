def clean(self):...
email = self.cleaned_data.get('email')
email_domain = email.split('@')[1].lower()
if email_domain != 'canada.ca':
message = forms.ValidationError(format(ErrorMessages.invalid_email_domain %
    email_domain))
if get_user_model().objects.filter(username=email.lower()).exists():
self.add_error('email', message)
message = forms.ValidationError(format(ErrorMessages.user_already_exists %
    email))
return self.cleaned_data
self.add_error('email', message)
