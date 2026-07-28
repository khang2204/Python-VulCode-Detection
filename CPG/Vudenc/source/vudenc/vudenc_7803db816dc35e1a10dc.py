def update_with_inherited_metadata(self, metadata):...
metadata.update({'source': metadata.get('source') or self.metadata('source'
    ), 'source_url': metadata.get('source_url') or self.metadata(
    'source_url'), 'license': metadata.get('license') or self.metadata(
    'license'), 'license_url': metadata.get('license_url') or self.metadata
    ('license_url'), 'about': metadata.get('about') or self.metadata(
    'about'), 'about_url': metadata.get('about_url') or self.metadata(
    'about_url')})
