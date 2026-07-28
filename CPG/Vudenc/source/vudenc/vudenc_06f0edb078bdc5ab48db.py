from flask import render_template, redirect, url_for, request, flash, abort, Markup, send_from_directory
from app import app, fbdb
from .forms import ProcessingForm, FILE_MAP
from . import utils
from shutil import copyfile, rmtree
import os
import tempfile
import requests
import subprocess as sub
@app.route('/')...
return render_template('index.html', title='GenSET')
