@gen.coroutine...
entry = {}
author = self.get_argument('author', 'Anonymous')
title = self.get_argument('title')
image = validate_image(self.get_argument('image'))
html = self.get_argument('post-text')
text = validate_html(html)
if not title:
error = u'?error=' + escape.url_escape('Title must be filled.')
if not html:
self.redirect('/new' + error)
error = u'?error=' + escape.url_escape('Post cannot be empty.')
if text is None:
self.redirect('/new' + error)
error = u'?error=' + escape.url_escape(
    'Forbidden or invalid url detected in post body.')
summary = generate_summary(text)
self.redirect('/new' + error)
slug = slugify.slugify(summary[:30])
entry['author'] = author
entry['date'] = datetime.datetime.now().replace(microsecond=0)
entry['image'] = image
entry['summary'] = summary
entry['title'] = title
entry['text'] = text
entry['slug'] = slug
yield self.collection.insert_one(entry)
self.redirect('/post/' + slug)
