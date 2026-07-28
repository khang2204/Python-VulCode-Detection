def split_filename(filename):...
"""docstring"""
is_epoch = True if filename.find(':') != -1 else False
if filename[-4:] == '.rpm':
filename = filename[:-4]
arch_index = filename.rfind('.')
arch = filename[arch_index + 1:]
rel_index = filename[:arch_index].rfind('-')
rel = filename[rel_index + 1:arch_index]
if is_epoch:
ver_index = filename[:rel_index].rfind(':')
ver_index = filename[:rel_index].rfind('-')
ver = filename[ver_index + 1:rel_index]
if is_epoch:
epoch_index = filename[:ver_index].rfind('-')
epoch_index = ver_index
epoch = filename[epoch_index + 1:ver_index]
epoch = '0'
name = filename[:epoch_index]
return name, ver, rel, epoch, arch
