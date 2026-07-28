def process(self, bracket, scene, display_name, new_bracket=False):...
sql = "SELECT * FROM analyzed WHERE base_url = '" + str(bracket) + "';"
result = self.db.exec(sql)
if len(result) > 0:
LOG.info('tried to analyze {}, but has already been done.'.format(bracket))
if 'smash.gg' in bracket:
return
success = get_results.process(bracket, scene, self.db, display_name)
html, status = bracket_utils.hit_url(bracket)
if success:
if status == 200 and bracket_utils.is_valid(html):
self.insert_placing_data(bracket, new_bracket)
LOG.exc('Analyzing smashgg tournament {} was not successful'.format(bracket))
get_results.process(bracket, scene, self.db, display_name)
self.insert_placing_data(bracket, new_bracket)
