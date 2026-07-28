@property...
if self.comment_english and translation.get_language() == LANGUAGE_CODE_EN:
return self.comment_english
return self.comment
