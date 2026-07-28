from datetime import date, time
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponseBadRequest
from frontpage.models import Profile, Media, MediaUpload
from frontpage.management.magic import compile_markdown, get_current_user
import logging
import ntpath
import os
import math
import PIL
from PIL import Image
PATH_TO_UPLOAD_FOLDER_ON_DISK: str = '/usr/local/www/focweb/'
IMAGE_SCALE = 64
def action_change_user_avatar(request: HttpRequest):...
user_id = int(request.GET['payload'])
return redirect('/admin?error=' + str(e))
return redirect('/admin/users')
media_id = int(request.GET['media_id'])
user: Profile = Profile.objects.get(pk=int(user_id))
u: Profile = get_current_user(request)
if not u == user and u.rights < 4:
return redirect("/admin?error='You're not allowed to edit other users.'")
medium = Media.objects.get(pk=int(media_id))
user.avatarMedia = medium
user.save()
