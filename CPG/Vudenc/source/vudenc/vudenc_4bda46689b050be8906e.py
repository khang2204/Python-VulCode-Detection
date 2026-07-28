def meetup_article_text(meetup):...
t = Template(filename='r2/templates/showmeetup.html', output_encoding=
    'utf-8', encoding_errors='replace')
res = t.get_def('meetup_info').render_unicode(meetup=meetup)
url = url_for(controller='meetups', action='show', id=meetup._id36)
title = python_websafe(meetup.title)
hdr = u"<h2>Discussion article for the meetup : <a href='%s'>%s</a></h2>" % (
    url, title)
return hdr + res + hdr
