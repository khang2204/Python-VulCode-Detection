def validate_image(image):...
checklist = ['gif', 'png', 'jpg']
if image[-3:].lower() in checklist:
return image
return 'http://ic.pics.livejournal.com/masio/8221809/287143/287143_original.gif'
