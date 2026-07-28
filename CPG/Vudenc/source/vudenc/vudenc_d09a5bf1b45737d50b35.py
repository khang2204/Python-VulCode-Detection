@query_cached...
result = [columns]
for entry in lore.io.bucket.objects.filter(Prefix=os.path.join(self.
temp = tempfile.NamedTemporaryFile()
return result
lore.io.bucket.download_file(entry.key, temp.name)
result += list(csv.reader(gz, delimiter='|', quotechar='"'))
