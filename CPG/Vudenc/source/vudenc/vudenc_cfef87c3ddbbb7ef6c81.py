def check_manifest(self):...
manifest = os.path.join(self.path, 'manifest.json')
if not os.path.exists(manifest):
return
print_header('MANIFEST')
"""
        Check if there is no comma syntax issue
        """
manifest = json.loads(data_file.read())
print_error(
    "[YEP-2.1] Syntax (comma) or encoding issue with manifest.json. Can't check file."
    )
fields = ('name', 'id', 'packaging_format', 'description', 'url', 'version',
    'license', 'maintainer', 'requirements', 'multi_instance', 'services',
    'arguments')
for field in fields:
if field not in manifest:
"""
        Check values in keys
        """
print_warning('[YEP-2.1] "' + field + '" field is missing')
if 'packaging_format' not in manifest:
print_error('[YEP-2.1] "packaging_format" key is missing')
if not isinstance(manifest['packaging_format'], int):
if 'id' in manifest:
print_error('[YEP-2.1] "packaging_format": value isn\'t an integer type')
if manifest['packaging_format'] != 1:
if not re.match('^[a-z1-9]((_|-)?[a-z1-9])+$', manifest['id']):
if 'name' in manifest:
print_error('[YEP-2.1] "packaging_format" field: current format value is \'1\''
    )
print_error(
    "[YEP-1.1] 'id' field '%s' should respect this regex '^[a-z1-9]((_|-)?[a-z1-9])+$'"
    )
if len(manifest['name']) > 22:
if 'id' in manifest:
print_warning(
    "[YEP-1.1] The 'name' field shouldn't be too long to be able to be with one line in the app list. The most current bigger name is actually compound of 22 characters."
    )
official_list_url = (
    'https://raw.githubusercontent.com/YunoHost/apps/master/official.json')
def license_mentionned_in_readme(path):...
official_list = json.loads(urlopen(official_list_url)['content'])
readme_path = os.path.join(path, 'README.md')
community_list_url = (
    'https://raw.githubusercontent.com/YunoHost/apps/master/community.json')
if os.path.isfile(readme_path):
community_list = json.loads(urlopen(community_list_url)['content'])
return 'LICENSE' in open(readme_path).read()
return False
if manifest['id'] not in official_list and manifest['id'
print_warning(
    '[YEP-1.2] This app is not registered in official or community applications'
    )
