def get(self, ann_id):...
if ann_id:
ann = Announce.by_id(ann_id, self.sql_session).scalar()
start = _to_int(self.get_argument('start', '0'), -1, 0, 10000000000000000000)
if not ann:
step = _to_int(self.get_argument('step', '12'), 0, 1, 20)
if ann.is_private and not self.is_group_user('Announcement Manager'):
search = self.get_argument('search', '')
atts = AttachmentList.by_ann_id(ann_id, self.sql_session).all()
group = self.get_argument('group', '')
self.ann_d = ann.to_dict()
author = self.get_argument('author', '')
self.ann_d['tags'] = AnnTag.get_ann_tags(ann_id, self.sql_session)
hours = _to_int(self.get_argument('hours', ''), 0, 1, 23999999976)
self.ann_d['atts'] = [att.to_dict() for att in atts]
if start == -1 or step == 0:
meta = {'title': self.ann_d['title'], 'uri': '/announce/%s' % self.ann_d[
    'id'], 'content': BeautifulSoup(markdown(self.ann_d['content']),
    'html.parser').text}
q = self.sql_session.query(Announce)
self.set_header('Cache-Control', 'max-age=300')
if search:
self.page_render(self.ann_d, 'announce.html', meta=meta)
q = q.filter(Announce.full_text_search(search))
q = q.order_by(Announce.created.desc())
if author:
q = q.filter(Announce.author_name == author)
if group:
q = q.filter(Announce.author_group_name == group)
if hours:
start_time = datetime.utcnow() - timedelta(hours=hours)
if not self.is_group_user('Announcement Manager'):
q = q.filter(Announce.created >= start_time)
q = q.filter(Announce.is_private == False)
total = q.count()
q = q.offset(start).limit(step)
anns = q.all()
groups = self.sql_session.query(Announce.author_group_name).group_by(Announce
    .author_group_name).all()
authors = self.sql_session.query(Announce.author_name).group_by(Announce.
    author_name).all()
def _make_ann(ann):...
_d = ann.to_dict()
_d['tags'] = AnnTag.get_ann_tags(ann.id, self.sql_session)
return _d
