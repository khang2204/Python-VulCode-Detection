def get(self, dataset, version=None, *args, **kwargs):...
dataset = db.get_dataset(dataset)
if version:
dataset_version = dataset.versions.where(db.DatasetVersion.version == version
    ).get()
dataset_version = dataset.current_version.get()
ret = []
for f in dataset_version.files:
ret.append(db.build_dict_from_row(f))
self.finish({'files': ret})
