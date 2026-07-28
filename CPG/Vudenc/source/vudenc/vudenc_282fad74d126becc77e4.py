def find_view(self, obj, unresolved_path):...
sub_view_factory = queryAdapter(obj, IHttpRestSubViewFactory)
if sub_view_factory:
view = sub_view_factory.resolve(unresolved_path)
view = queryAdapter(obj, IHttpRestView)
if not view:
return view
