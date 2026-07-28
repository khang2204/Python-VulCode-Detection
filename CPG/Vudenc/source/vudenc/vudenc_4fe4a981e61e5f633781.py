def settingsToHtmlForm():...
settingsInputs = []
for sectionSettingsPair in settings.settingsStructure:
settingsInputs.append('<h2>{}</h2>'.format(sectionSettingsPair[0]))
return ''.join(settingsInputs)
for sectionOption in sectionSettingsPair[1]:
option = None
optionComment = ''
if type(sectionOption) == tuple:
option = sectionOption[0]
option = sectionOption
optionComment = '<p class="optionComment">{}</p>'.format(sectionOption[1])
if type(settings.settings[option]) == bool:
settingsInputs.append(
    """<label for="{option}">{optionName}</label>
                                     <input type="checkbox" id="{option}" name="{option}" value="{optionValue}" {checkedState} />{comment}
                                     <br />"""
    .format(option=option, optionName=option.replace('_', ' '), comment=
    optionComment, checkedState='checked' if settings.settings[option] else
    '', optionValue='1' if settings.settings[option] else '0'))
if type(settings.settings[option]) == int:
settingsInputs.append(
    """<label for="{option}">{optionName}</label>
                                     <input type="number" id="{option}" name="{option}" value="{optionValue}" />{comment}
                                     <br />"""
    .format(option=option, optionName=option.replace('_', ' '), comment=
    optionComment, optionValue=settings.settings[option]))
if type(settings.settings[option]) == str:
settingsInputs.append(
    """<label for="{option}">{optionName}</label>
                                     <input type="{type}" id="{option}" name="{option}" value="{optionValue}" />{comment}
                                     <br />"""
    .format(option=option, optionName=option.replace('_', ' '), comment=
    optionComment, optionValue=settings.settings[option], type='password' if
    'secret' in option.lower() or 'password' in option.lower() else 'text'))
