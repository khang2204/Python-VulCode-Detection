def field_error(e):...
_ = re.compile('UNIQUE constraint failed: (.*)$')
m = _.match(str(e))
error = {'blog.local_path':
    """
The file path for this blog is the same as another blog in this system.
File paths must be unique.
"""
    , 'blog.url':
    """
The URL for this blog is the same as another blog in this system.
URLs for blogs must be unique.
"""
    }[m.group(1)]
return error
