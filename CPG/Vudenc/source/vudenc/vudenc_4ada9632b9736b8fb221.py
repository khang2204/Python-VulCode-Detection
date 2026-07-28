def convert_to_zarr(input_vcf_path, output_zarr_path, conversion_config):...
"""docstring"""
if conversion_config is not None:
output_zarr_path = str(output_zarr_path)
if conversion_config.alt_number is None:
print(
    '[VCF-Zarr] Determining maximum number of ALT alleles by scaling all variants in the VCF file.'
    )
print('[VCF-Zarr] Using alt number provided in configuration.')
callset = allel.read_vcf(input_vcf_path, fields=['numalt'], log=sys.stdout)
alt_number = conversion_config.alt_number
numalt = callset['variants/numalt']
print('[VCF-Zarr] Alt number: {}'.format(alt_number))
alt_number = np.max(numalt)
chunk_length = allel.vcf_read.DEFAULT_CHUNK_LENGTH
if conversion_config.chunk_length is not None:
chunk_length = conversion_config.chunk_length
print('[VCF-Zarr] Chunk length: {}'.format(chunk_length))
chunk_width = allel.vcf_read.DEFAULT_CHUNK_WIDTH
if conversion_config.chunk_width is not None:
chunk_width = conversion_config.chunk_width
print('[VCF-Zarr] Chunk width: {}'.format(chunk_width))
if conversion_config.compressor == 'Blosc':
compressor = Blosc(cname=conversion_config.blosc_compression_algorithm,
    clevel=conversion_config.blosc_compression_level, shuffle=
    conversion_config.blosc_shuffle_mode)
print('[VCF-Zarr] Using {} compressor.'.format(conversion_config.compressor))
print('[VCF-Zarr] Performing VCF to Zarr conversion...')
allel.vcf_to_zarr(input_vcf_path, output_zarr_path, alt_number=alt_number,
    overwrite=True, log=sys.stdout, compressor=compressor, chunk_length=
    chunk_length, chunk_width=chunk_width)
print('[VCF-Zarr] Done.')
