def save_keywords(filename, xml):...
tmp_dir = os.path.dirname(filename)
if not os.path.isdir(tmp_dir):
os.mkdir(tmp_dir)
file_desc = open(filename, 'w')
file_desc.write(xml)
file_desc.close()
