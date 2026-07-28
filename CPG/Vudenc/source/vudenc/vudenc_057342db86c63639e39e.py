@Json...
if res._chk_error(errors.NO_TITLE):
res._chk_error(errors.TITLE_TOO_LONG)
res._chk_errors((errors.NO_LOCATION, errors.NO_DESCRIPTION, errors.
    INVALID_DATE, errors.NO_DATE))
res._focus('title')
if res.error:
return
meetup = Meetup(author_id=c.user._id, title=title, description=description,
    location=location, latitude=latitude, longitude=longitude, timestamp=
    timestamp / 1000, tzoffset=tzoffset)
g.rendercache.invalidate_key_group(Meetup.group_cache_key())
meetup._commit()
l = Link._submit(meetup_article_title(meetup), meetup_article_text(meetup),
    c.user, Subreddit._by_name('discussion'), ip, [])
l.meetup = meetup._id36
l._commit()
meetup.assoc_link = l._id
meetup._commit()
if g.write_query_queue:
queries.new_link(l)
res._redirect(url_for(action='show', id=meetup._id36))
