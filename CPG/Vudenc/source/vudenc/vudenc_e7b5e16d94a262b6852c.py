@redirect_ui_on_replica...
"""docstring"""
doc_types = []
def add_doc_type(tp):...
"""docstring"""
if not tp:
return None
if isinstance(tp, basestring):
for d in self.doc_types:
if not any(d['name'] == tp['name'] for d in doc_types):
if d['name'] == tp:
tp = tp.copy()
return tp['name']
tp = d
tp['example'] = json.dumps(tp['example'], sort_keys=True, separators=(', ',
    ': '), indent=2)
doc_types.append(tp)
