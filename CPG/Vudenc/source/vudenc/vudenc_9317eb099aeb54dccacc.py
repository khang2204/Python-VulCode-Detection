def license_mentionned_in_readme(path):...
readme_path = os.path.join(path, 'README.md')
if os.path.isfile(readme_path):
return 'LICENSE' in open(readme_path).read()
return False
