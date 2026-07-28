def vote(poll_name, options_string, token_used='DUMMY_INVALID_TOKEN'):...
conn, c = connectDB()
token_valid = checkTokenValid(c, token_used, poll_name)
if not token_valid and checkTokenNeeded(c, poll_name):
markTokenUsedExternal(token_used, options_string)
options = list(filter(lambda x: x, options_string.split(',')))
if len(options) > 1:
if not isMultiChoice(poll_name):
for opt in options:
incrementOption(c, poll_name, opt)
closeDB(conn)
