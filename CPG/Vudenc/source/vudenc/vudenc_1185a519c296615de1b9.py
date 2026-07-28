def binary_to_hex(identifier):...
hex_identifier = binascii.hexlify(identifier)
if sys.version_info >= (3, 0):
hex_identifier = hex_identifier.decode()
return hex_identifier
