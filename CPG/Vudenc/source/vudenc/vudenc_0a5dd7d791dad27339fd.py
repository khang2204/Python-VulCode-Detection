def find_ftdi_serials():...
debuggers = Context().list_devices(ID_VENDOR_ID='0403', ID_MODEL_ID='6014')
serials = []
for debugger in debuggers:
if 'DEVLINKS' not in debugger:
return serials
serials.append(debugger['ID_SERIAL_SHORT'])
