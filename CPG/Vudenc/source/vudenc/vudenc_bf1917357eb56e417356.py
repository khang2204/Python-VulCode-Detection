def _AddSyntaxDataIfNeeded(self, extra_data):...
if not self._user_options['seed_identifiers_with_syntax']:
return
filetype = vimsupport.CurrentFiletypes()[0]
if filetype in self._filetypes_with_keywords_loaded:
return
self._filetypes_with_keywords_loaded.add(filetype)
extra_data['syntax_keywords'] = list(syntax_parse.
    SyntaxKeywordsForCurrentBuffer())
