@register.inclusion_tag('news/user_news.html', takes_context=True)...
if not 'instance' in context:
if not 'now' in context:
context['now'] = timezone.now()
if not 'course_news' in context:
context['course_news'] = CachedNews(context['instance'])
news = context['course_news']
if context['is_course_staff']:
alerts, news = news.for_staff()
user = context['request'].user
i = 0
alerts, news = news.for_user(not user.is_authenticated() or user.
    userprofile.is_external)
for item in news:
i += 1
return {'is_course_staff': context['is_course_staff'], 'now': context['now'
    ], 'alerts': alerts, 'news': news, 'more': more}
item['collapsed'] = i > num
if more > 0 and i == more:
item['begin_more'] = True
