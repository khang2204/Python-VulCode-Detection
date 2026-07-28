def url_from_directory(directory, include_commit=True):...
if exists(join(directory, '.svn')):
cls = SvnSubproject
if exists(join(directory, '.git')):
return cls.url_from_directory(directory, include_commit)
cls = GitSubproject
