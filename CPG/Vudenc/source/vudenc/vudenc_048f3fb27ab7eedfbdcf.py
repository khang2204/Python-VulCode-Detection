def _make_ann(ann):...
_d = ann.to_dict()
_d['tags'] = AnnTag.get_ann_tags(ann.id, self.sql_session)
return _d
