def preview_file_old(filename, extension):...
import zlib
split_path = filename.rsplit('/', 1)[1]
split_path = filename
return 'preview-' + str(zlib.crc32(split_path.encode('utf-8'), 65535)
    ) + '.' + extension
