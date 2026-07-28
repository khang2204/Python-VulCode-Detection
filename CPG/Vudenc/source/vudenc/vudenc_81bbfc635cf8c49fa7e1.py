@Json...
if res._chk_error(errors.NO_TITLE):
res._chk_error(errors.TITLE_TOO_LONG)
res._chk_errors((errors.NO_LOCATION, errors.NO_DESCRIPTION, errors.
    INVALID_DATE, errors.NO_DATE))
res._focus('title')
if res.error:
return
meetup.title = title
meetup.description = description
meetup.location = location
meetup.latitude = latitude
meetup.longitude = longitude
meetup.timestamp = timestamp / 1000
meetup.tzoffset = tzoffset
g.rendercache.invalidate_key_group(Meetup.group_cache_key())
meetup._commit()
article = Link._byID(meetup.assoc_link)
article._load()
article_old_url = article.url
article.title = meetup_article_title(meetup)
article.article = meetup_article_text(meetup)
article._commit()
article.update_url_cache(article_old_url)
res._redirect(url_for(action='show', id=meetup._id36))
