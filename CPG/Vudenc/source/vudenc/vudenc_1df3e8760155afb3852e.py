@tornado.web.authenticated...
currentOutputDir = settings.settings['Output_dir']
print('Received new settings')
for option in settings.settings:
newValue = self.get_argument(option, None)
settings.writeServerSettings()
if not newValue:
self.doSettings(True)
if type(settings.settings[option]) == bool:
if type(settings.settings[option]) == bool:
if currentOutputDir != settings.settings['Output_dir']:
settings.settings[option] = False
print(
    """Warning: Option {} unset! The settingsStructure might be out of sync.
	Ignore this if the field is intentionally empty"""
    .format(option))
newValue = True
if type(settings.settings[option]) == int:
generateSavedImagesCache(settings.settings['Output_dir'])
settings.settings[option] = newValue
newValue = int(newValue)
