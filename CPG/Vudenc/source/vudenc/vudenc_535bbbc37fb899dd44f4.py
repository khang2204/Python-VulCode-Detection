def clean(self):...
email = self.cleaned_data.get('email').lower()
password = self.cleaned_data.get('password')
user = authenticate(username=email, password=password)
if user is None:
message = forms.ValidationError(ErrorMessages.invalid_un_or_pw)
if user.email_confirmed is False:
self.add_error('email', message)
message = forms.ValidationError(ErrorMessages.unconfirmed_email)
return self.cleaned_data
self.add_error('email', message)
