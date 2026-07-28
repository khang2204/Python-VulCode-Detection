def find_uart_serials():...
uarts = Context().list_devices(ID_VENDOR_ID='04b4', ID_MODEL_ID='0008')
serials = {}
for uart in uarts:
if 'DEVLINKS' in uart:
return serials
serials[uart['DEVNAME']] = uart['ID_SERIAL_SHORT']
