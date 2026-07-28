def updateScriptStatus():...
if not runScriptWebSocketConnections or not scriptPipeConnection or not scriptPipeConnection.poll(
return
pipeOutput = scriptPipeConnection.recv()
if pipeOutput:
responseMessage = '{{"message":"{}", "action":"{}"}}'.format(pipeOutput.
    replace('\n', '\\n').replace('\t', ''), 'printMessage')
for client in runScriptWebSocketConnections:
client.write_message(responseMessage)
if redditUserImageScraper.scriptFinishedSentinel in pipeOutput:
print('Refreshing cache due to script finishing')
generateSavedImagesCache(settings.settings['Output_dir'])
responseMessage = '{{"action":"{}"}}'.format('scriptFinished')
for client in runScriptWebSocketConnections:
client.write_message(responseMessage)
scriptPipeConnection.close()
