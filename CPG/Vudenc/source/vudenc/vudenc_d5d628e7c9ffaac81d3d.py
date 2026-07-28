def save_model(self, request, obj, form, change):...
if 'internet_nl_api_password' in form.changed_data:
f = Fernet(settings.FIELD_ENCRYPTION_KEY)
super().save_model(request, obj, form, change)
encrypted = f.encrypt(obj.internet_nl_api_password.encode())
obj.internet_nl_api_password = encrypted
