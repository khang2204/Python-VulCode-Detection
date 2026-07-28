def Log(user, message, logLevel):...
if logLevel == 0:
logLevel = 'INFO : '
if logLevel == 1:
discordLogLevel = 'INFO : '
logLevel = '! WARNING : '
logLevel = '!! ERROR : '
i = datetime.now()
discordLogLevel = '**WARNING : **'
discordLogLevel = '__**ERROR : **__'
date = i.strftime('%Y/%m/%d %H:%M:%S')
LogFile = open(constants.Paths.logsFile, 'a')
fileOutput = str(logLevel) + str(date) + ' -' + str(user) + ' : ' + str(message
    )
LogFile.write(fileOutput + '\n')
discordOutput = str(discordLogLevel) + str(date) + ' -' + str(user
    ) + ' : ' + str(message)
LogFile.close()
return discordOutput
