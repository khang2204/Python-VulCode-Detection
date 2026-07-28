from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
import magic, mimetypes
from .models import ScreenDoorUser, Position, Applicant
from .uservisibletext import ErrorMessages, CreatePositionFormText, CreateAccountFormText, StandardFormText, LoginFormText
model = Applicant
fields = 'pdf',
text = CreatePositionFormText.upload_new_position
description = CreatePositionFormText.please_select_either_filetype
pdf_name = CreatePositionFormText.pdf
url_name = CreatePositionFormText.url
pdf_text = CreatePositionFormText.browse_for_pdf
url_text = CreatePositionFormText.link_to_job_description
upload_text = CreatePositionFormText.choose_a_file
browse_text = CreatePositionFormText.browse
submit_text = CreatePositionFormText.submit
model = Position
fields = 'pdf', 'url_ref'
widgets = {'url_ref': forms.TextInput(attrs={'disabled': 'disabled'})}
def clean(self):...
pdf = self.cleaned_data.get('pdf')
url = self.cleaned_data.get('url_ref')
if not pdf and not url:
msg = forms.ValidationError(ErrorMessages.empty_create_position_form)
if pdf and url:
self.add_error('pdf', msg)
msg = forms.ValidationError(ErrorMessages.overfilled_create_position_form)
if pdf:
return
self.add_error('pdf', msg)
file_type = mimetypes.MimeTypes().types_map_inv[1][magic.from_buffer(self.
    cleaned_data['pdf'].read(), mime=True)][0]
if url:
return
if not file_type == '.pdf':
msg = forms.ValidationError(ErrorMessages.url_upload_not_supported_yet)
return self.cleaned_data
msg = forms.ValidationError(ErrorMessages.incorrect_mime_type)
self.add_error('url_ref', msg)
self.add_error('pdf', msg)
