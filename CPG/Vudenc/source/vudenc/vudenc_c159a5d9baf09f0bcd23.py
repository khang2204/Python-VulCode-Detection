def CurrentFiletypeCompletionEnabled(self):...
filetypes = vimsupport.CurrentFiletypes()
filetype_to_disable = self._user_options[
    'filetype_specific_completion_to_disable']
return not all([(x in filetype_to_disable) for x in filetypes])
