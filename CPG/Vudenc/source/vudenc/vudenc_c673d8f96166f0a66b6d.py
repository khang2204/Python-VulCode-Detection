def setup_vcf_to_zarr(input_vcf_dir, output_zarr_dir, conversion_config):...
"""docstring"""
input_vcf_dir = str(input_vcf_dir)
output_zarr_dir = str(output_zarr_dir)
create_directory_tree(input_vcf_dir)
create_directory_tree(output_zarr_dir)
pathlist_vcf = pathlib.Path(input_vcf_dir).glob('**/*.vcf')
for path in pathlist_vcf:
path_str = str(path)
file_output_str = path_leaf(path_str)
file_output_str = file_output_str[0:len(file_output_str) - 4]
path_zarr_output = str(pathlib.Path(output_zarr_dir, file_output_str))
print('[Setup][Data] Converting VCF file to Zarr format: {}'.format(path_str))
print('  - Output: {}'.format(path_zarr_output))
convert_to_zarr(input_vcf_path=path_str, output_zarr_path=path_zarr_output,
    conversion_config=conversion_config)
