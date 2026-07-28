def get_user(self):...
email = self.cleaned_data.get('email').lower()
password = self.cleaned_data.get('password')
return authenticate(username=email, password=password)
