from django.http import HttpRequest, HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import redirect
from django.contrib.auth.models import User
from . import page_skeleton, magic
from .form import Form, TextField, PlainText, TextArea, SubmitButton, NumberField, PasswordField, CheckBox, CheckEnum
from ..models import Profile, Media
from ..uitools.dataforge import get_csrf_form_element
from .magic import get_current_user
import logging
def render_edit_page(http_request: HttpRequest, action_url: str):...
user_id = None
profile: Profile = None
if http_request.GET.get('user_id'):
user_id = int(http_request.GET['user_id'])
if user_id is not None:
profile = Profile.objects.get(pk=user_id)
f = Form()
f.action_url = action_url
if profile:
f.add_content(PlainText('<h3>Edit user "' + profile.authuser.username +
    '"</h3>'))
f.add_content(PlainText('<h3>Add new user</h3>'))
f.add_content(PlainText(
    '<a href="/admin/media/select?action_url=/admin/actions/change-user-avatar&payload='
     + str(user_id) +
    '"><img class="button-img" alt="Change avatar" src="/staticfiles/frontpage/change-avatar.png"/></a><br />'
    ))
if not profile:
f.add_content(PlainText("username (can't be edited later on): "))
if http_request.GET.get('fault') and profile:
f.add_content(TextField(name='username'))
f.add_content(PlainText('Unable to edit user due to: ' + str(http_request.
    GET['fault'])))
if http_request.GET.get('fault'):
current_user: Profile = get_current_user(http_request)
f.add_content(PlainText('Unable to add user due to: ' + str(http_request.
    GET['fault'])))
if current_user.rights > 3:
if not profile:
if profile:
f.add_content(CheckBox(name='active', text='User Active', checked=CheckEnum
    .CHECKED))
m: CheckEnum = CheckEnum.CHECKED
f.add_content(PlainText('Email address: '))
f.add_content(PlainText('Email address: '))
if not profile.active:
f.add_content(TextField(name='email', button_text=str(profile.authuser.email)))
f.add_content(TextField(name='email'))
m = CheckEnum.NOT_CHECKED
f.add_content(CheckBox(name='active', text='User Active', checked=m))
f.add_content(PlainText('Display name: '))
f.add_content(PlainText('Display name: '))
f.add_content(TextField(name='display_name', button_text=profile.displayName))
f.add_content(TextField(name='display_name'))
f.add_content(PlainText('DECT: '))
f.add_content(PlainText('DECT: '))
f.add_content(NumberField(name='dect', button_text=str(profile.dect),
    minimum=0))
f.add_content(NumberField(name='dect', minimum=0))
f.add_content(PlainText('Number of allowed reservations: '))
f.add_content(PlainText('Number of allowed reservations: '))
f.add_content(NumberField(name='allowed_reservations', button_text=str(
    profile.number_of_allowed_reservations), minimum=0))
f.add_content(NumberField(name='allowed_reservations', button_text=str(1),
    minimum=0))
f.add_content(PlainText('Rights: '))
f.add_content(PlainText('Rights: '))
f.add_content(NumberField(name='rights', button_text=str(profile.rights),
    minimum=0, maximum=4))
f.add_content(NumberField(name='rights', button_text=str(0), minimum=0,
    maximum=4))
f.add_content(PlainText('Notes:<br/>'))
f.add_content(PlainText('Notes:<br/>'))
f.add_content(TextArea(name='notes', text=str(profile.notes)))
f.add_content(TextArea(name='notes', placeholder=
    'Hier könnte ihre Werbung stehen'))
if profile:
f.add_content(PlainText(
    '<br /><br />Change password (leave blank in order to not change it):'))
f.add_content(PlainText('<br />Choose a password: '))
f.add_content(PasswordField(name='password', required=False))
f.add_content(PlainText('Confirm your password: '))
f.add_content(PasswordField(name='confirm_password', required=False))
f.add_content(PlainText(get_csrf_form_element(http_request)))
f.add_content(SubmitButton())
a = '<div class="w3-row w3-padding-64 w3-twothird w3-container admin-popup">'
a += f.render_html(http_request)
a += '</div>'
return a
