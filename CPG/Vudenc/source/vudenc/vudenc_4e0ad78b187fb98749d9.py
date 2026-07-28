from os.path import join
from datetime import datetime
from flask import request, redirect, url_for, render_template, flash, g, current_app
from werkzeug.utils import secure_filename
from flask_security import login_required, current_user
from benwaonline.database import db
from benwaonline.models import Post, Tag, Comment, Preview, Image
from benwaonline.gallery import gallery
from benwaonline.gallery.forms import CommentForm, PostForm
@gallery.before_request...
g.user = current_user
@gallery.route('/gallery/')...
if tags == 'all':
posts = Post.query.all()
split = tags.split(' ')
tags = Tag.query.all()
posts = []
return render_template('gallery.html', posts=posts, tags=tags)
for s in split:
results = Post.query.filter(Post.tags.any(name=s))
posts.extend(results)
