def getTitle(submission):...
delimChars = ['-', ':', '=', '#', '(', ')']
title = str(submission.title)
for delimChar in delimChars:
title = title.split(delimChar)[0]
return str(''.join(re.findall('[a-zA-Z]', title)).lower())
