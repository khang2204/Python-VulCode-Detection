def run(self, lang):...
if lang:
lang = str(lang.split('[')[1].strip(']'))
return 'en'
if lang in g.all_languages:
return lang
