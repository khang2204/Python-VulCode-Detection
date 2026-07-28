def isUserAuthorized():...
username, password = getUsernameAndPassword()
response = usr.validateCredentials(username, password, mysql)
return response
