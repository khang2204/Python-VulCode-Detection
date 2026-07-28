def process_data_files(input_dir, temp_dir, output_dir):...
"""docstring"""
input_dir = str(input_dir)
temp_dir = str(temp_dir)
output_dir = str(output_dir)
create_directory_tree(input_dir)
create_directory_tree(temp_dir)
create_directory_tree(output_dir)
pathlist_gz = pathlib.Path(input_dir).glob('**/*.gz')
for path in pathlist_gz:
path_str = str(path)
pathlist_vcf_temp = pathlib.Path(temp_dir).glob('**/*.vcf')
file_output_str = path_leaf(path_str)
for path in pathlist_vcf_temp:
file_output_str = file_output_str[0:len(file_output_str) - 3]
path_temp_str = str(path)
remove_directory_tree(temp_dir)
path_temp_output = str(pathlib.Path(temp_dir, file_output_str))
filename_str = path_leaf(path_temp_str)
pathlist_vcf_input = pathlib.Path(input_dir).glob('**/*.vcf')
print('[Setup][Data] Decompressing file: {}'.format(path_str))
path_vcf_str = str(pathlib.Path(output_dir, filename_str))
for path in pathlist_vcf_input:
print('  - Output: {}'.format(path_temp_output))
shutil.move(path_temp_str, path_vcf_str)
path_input_str = str(path)
decompress_gzip(path_str, path_temp_output)
filename_str = path_leaf(path_input_str)
path_vcf_str = str(pathlib.Path(output_dir, filename_str))
shutil.copy(path_input_str, path_vcf_str)
