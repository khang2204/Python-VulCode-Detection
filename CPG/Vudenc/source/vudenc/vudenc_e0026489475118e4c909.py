def setup(self, request, *args, **kwargs):...
"""docstring"""
self.params = utils.Struct()
self.read_params(get_params=BaseView._GET_PARAMETERS)
self.env = utils.Struct()
self.env.repo = kwargs.get('repo', None)
self.env.action = self.ACTION_ID
self.env.config = config.Configuration(self.env.repo or '*')
lang = self.params.get('lang') or self.request.LANGUAGE_CODE
lang = re.sub('[^A-Za-z0-9-]', '', lang)
lang = const.LANGUAGE_SYNONYMS.get(lang, lang)
if lang in const.LANGUAGE_ENDONYMS.keys():
self.env.lang = lang
self.env.lang = self.env.config.language_menu_options[0
    ] if self.env.config.language_menu_options else const.DEFAULT_LANGUAGE_CODE
self.env.rtl = self.env.lang in const.LANGUAGES_BIDI
self.env.charset = const.CHARSET_UTF8
self.env.global_url = self.build_absolute_uri('/global')
