def get(self, dataset, *args, **kwargs):...
user = self.current_user
dataset = db.get_dataset(dataset)
collections = {}
for sample_set in dataset.sample_sets:
collection = sample_set.collection
ret = {'collections': collections, 'study': db.build_dict_from_row(dataset.
    study)}
if not collection.name in collections:
ret['study']['publication_date'] = ret['study']['publication_date'].strftime(
    '%Y-%m-%d')
collections[collection.name] = {'sample_sets': [], 'ethnicity': collection.
    ethnicity}
collections[collection.name]['sample_sets'].append(db.build_dict_from_row(
    sample_set))
self.finish(ret)
