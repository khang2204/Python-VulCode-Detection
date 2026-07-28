def get_common_objects(self):...
super().get_common_objects()
lang = '_' + get_language().lower()
key = make_template_fragment_key('privacy_notice', [lang])
privacy_text = cache.get(key)
if not privacy_text:
template_name = 'privacy_notice{}.html'
self.privacy_text = privacy_text
template = try_get_template(template_name.format(lang))
self.note('privacy_text')
if not template and len(lang) > 3:
template = try_get_template(template_name.format(lang[:3]))
if not template:
logger.warning('No localized privacy notice for language %s', lang)
if not template:
template = try_get_template(template_name.format(''))
logger.error('No privacy notice at all!')
privacy_text = template.render() if template else _(
    'No privacy notice. Please notify administration!')
cache.set(key, privacy_text)
