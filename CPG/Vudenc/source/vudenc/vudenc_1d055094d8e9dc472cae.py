def get_tmp_file(recid):...
tmp_directory = '%s/bibclassify' % bconfig.CFG_TMPDIR
if not os.path.isdir(tmp_directory):
os.mkdir(tmp_directory)
filename = 'bibclassify_%s.xml' % recid
abs_path = os.path.join(tmp_directory, filename)
return abs_path
