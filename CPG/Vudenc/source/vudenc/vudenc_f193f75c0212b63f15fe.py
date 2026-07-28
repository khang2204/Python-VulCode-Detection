from reddit_base import RedditController
from r2.lib.pages import BoringPage, ShowMeetup, NewMeetup, EditMeetup, PaneStack, CommentListing, LinkInfoPage, CommentReplyBox, NotEnoughKarmaToPost
from validator import validate, VUser, VRequired, VMeetup, VEditMeetup, VFloat, ValueOrBlank, ValidIP, VMenu, VCreateMeetup
from errors import errors
from r2.lib.jsonresponse import Json
from routes.util import url_for
from r2.models import Meetup, Link, Subreddit, CommentBuilder
from r2.models.listing import NestedListing
from r2.lib.menus import CommentSortMenu, NumCommentsMenu
from r2.lib.filters import python_websafe
from mako.template import Template
from pylons.i18n import _
from pylons import c, g, request
import json
def meetup_article_text(meetup):...
t = Template(filename='r2/templates/showmeetup.html', output_encoding=
    'utf-8', encoding_errors='replace')
res = t.get_def('meetup_info').render_unicode(meetup=meetup)
url = url_for(controller='meetups', action='show', id=meetup._id36)
title = python_websafe(meetup.title)
hdr = u"<h2>Discussion article for the meetup : <a href='%s'>%s</a></h2>" % (
    url, title)
return hdr + res + hdr
