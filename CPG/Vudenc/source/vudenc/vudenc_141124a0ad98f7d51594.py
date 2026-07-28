def csrf_tag(csrf):...
"""docstring"""
return "<input type='hidden' name='csrf' id='csrf' value='{}'>".format(
    csrf_hash(csrf))
