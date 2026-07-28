def preview_file(identifier, extension):...
file_identifier = 'preview-{}'.format(identifier)
import zlib
return 'preview-' + str(zlib.crc32(file_identifier.encode('utf-8'), 65535)
    ) + '.' + extension
