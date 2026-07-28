def formatReply(result):...
if result[2] == '':
reply = result[0] + ' is ' + result[1] + '.'
if result[0][2] != '' and result[2]:
return reply
reply = result[0] + ' brewed in ' + result[2] + ' is ' + result[1] + '.'
