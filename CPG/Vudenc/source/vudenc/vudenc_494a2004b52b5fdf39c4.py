@query_cached...
frames = []
for entry in lore.io.bucket.objects.filter(Prefix=os.path.join(self.
temp = tempfile.NamedTemporaryFile()
result = pandas.concat(frames)
lore.io.bucket.download_file(entry.key, temp.name)
result.columns = columns
dataframe = pandas.read_csv(temp.name, delimiter='|', quotechar='"',
    compression='gzip', error_bad_lines=False)
buffer = StringIO()
dataframe.columns = columns
result.info(buf=buffer, memory_usage='deep')
frames.append(dataframe)
logger.info(buffer.getvalue())
logger.info(result.head())
return result
