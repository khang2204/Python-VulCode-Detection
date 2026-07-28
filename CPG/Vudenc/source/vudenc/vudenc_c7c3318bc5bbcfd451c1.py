def _make_user_csv(self):...
users = User.objects.all()
user_dicts = [{'name': u.name, 'email': u.email, 'joined': u.date_joined} for
    u in users]
stringio = io.StringIO()
csv_writer = csv.DictWriter(stringio, user_dicts[0].keys())
csv_writer.writeheader()
for user_dict in user_dicts:
csv_writer.writerow(user_dict)
return stringio.getvalue()
