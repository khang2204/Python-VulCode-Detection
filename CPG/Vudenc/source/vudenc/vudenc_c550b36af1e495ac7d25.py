def _main():...
input_directory = './data/input/'
download_directory = input_directory + 'download/'
temp_directory = './data/temp/'
vcf_directory = './data/vcf/'
zarr_directory_setup = './data/zarr/'
zarr_directory_benchmark = './data/zarr_benchmark/'
cli_arguments = get_cli_arguments()
command = cli_arguments['command']
if command == 'config':
output_config_location = cli_arguments['output_config']
if command == 'setup':
overwrite_mode = cli_arguments['f']
print('[Setup] Setting up benchmark data.')
if command == 'exec':
config.generate_default_config_file(output_location=output_config_location,
    overwrite=overwrite_mode)
data_service.remove_directory_tree(vcf_directory)
print('[Exec] Executing benchmark tool.')
print('Error: Unexpected command specified. Exiting...')
data_service.remove_directory_tree(zarr_directory_setup)
runtime_config = config.read_configuration(location=cli_arguments[
    'config_file'])
sys.exit(1)
runtime_config = config.read_configuration(location=cli_arguments[
    'config_file'])
vcf_to_zarr_config = config.VCFtoZarrConfigurationRepresentation(runtime_config
    )
ftp_config = config.FTPConfigurationRepresentation(runtime_config)
if ftp_config.enabled:
print('[Setup][FTP] FTP module enabled. Running FTP download...')
print('[Setup][FTP] FTP module disabled. Skipping FTP download...')
data_service.fetch_data_via_ftp(ftp_config=ftp_config, local_directory=
    download_directory)
data_service.process_data_files(input_dir=input_directory, temp_dir=
    temp_directory, output_dir=vcf_directory)
vcf_to_zarr_config = config.VCFtoZarrConfigurationRepresentation(runtime_config
    )
if vcf_to_zarr_config.enabled:
data_service.setup_vcf_to_zarr(input_vcf_dir=vcf_directory, output_zarr_dir
    =zarr_directory_setup, conversion_config=vcf_to_zarr_config)
