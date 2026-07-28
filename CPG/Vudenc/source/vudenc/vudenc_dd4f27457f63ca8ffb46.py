from django.shortcuts import render
from django.db import transaction
from django.core import serializers
from django.http import HttpResponse
from sio.models import *
from sio.forms import *
def make_view(request, messages=[], create_student_form=CreateStudentForm(),...
context = {'courses': Course.objects.all(), 'messages': messages,
    'create_student_form': create_student_form, 'create_course_form':
    create_course_form, 'register_student_form': register_student_form}
return render(request, 'sio.html', context)
