def create_node(self, *args, **kwargs):...
metadata_store = MetadataStore(os.path.join(self.temporary_directory(), 
    '%d.db' % self.count), self.temporary_directory(), default_eccrypto.
    generate_key(u'curve25519'))
kwargs['metadata_store'] = metadata_store
node = super(TestGigaChannelUnits, self).create_node(*args, **kwargs)
self.count += 1
return node
