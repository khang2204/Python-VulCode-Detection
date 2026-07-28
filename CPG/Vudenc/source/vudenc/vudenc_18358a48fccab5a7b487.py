def get_list_of_named_scenes():...
austin = constants.AUSTIN_URLS
smashbrews = constants.SMASHBREWS_RULS
colorado_singles = constants.COLORADO_SINGLES_URLS
colorado_doubles = constants.COLORADO_DOUBLES_URLS
sms = constants.SMS_URLS
base_urls = [['sms', sms], ['smashbrews', smashbrews], ['austin', austin],
    ['colorado', colorado_singles], ['colorado_doubles', colorado_doubles]]
return base_urls
