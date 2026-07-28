def replyToUnansweredDMs(dms):...
for dm in dms:
results = getAlcoholByName(dm.text)
if len(results) > 10:
replyToDm = (
    'Sorry but I know a lot of alcohol with that in the name, could you be more specific?'
    )
if results == []:
api.send_direct_message(screen_name=dm.sender_screen_name, text=replyToDm)
replyToDm = (
    'Unfortunately I cannot find the name of the alcohol you specified in my database, apologies.'
    )
for result in results:
print(dm.sender_screen_name + ' sent ' + dm.text)
api.send_direct_message(screen_name=dm.sender_screen_name, text=replyToDm)
replyToDm = formatReply(result)
setLastReplied('DM', dm.id_str)
api.send_direct_message(screen_name=dm.sender_screen_name, text=replyToDm)
