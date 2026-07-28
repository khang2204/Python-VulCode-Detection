def on_message(self, message):...
if not login_get_current_user(self):
return None
print('RunScriptWebSocket: Received message ', message)
parsedMessage = json.loads(message)
command = parsedMessage['command']
print('RunScriptWebSocket: Command ', command)
if command == 'runScript':
if scriptProcess and scriptProcess.is_alive():
print('RunScriptWebSocket: Script already running')
print('RunScriptWebSocket: Starting script')
responseMessage = '{{"message":"{}", "action":"{}"}}'.format(
    'Script already running\\n', 'printMessage')
startScript()
self.write_message(responseMessage)
responseMessage = '{{"message":"{}", "action":"{}"}}'.format(
    'Running script\\n', 'printMessage')
self.write_message(responseMessage)
