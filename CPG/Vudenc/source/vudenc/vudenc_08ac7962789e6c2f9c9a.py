def get_submission_info(self):...
soup = BeautifulSoup(self.res_data, 'html.parser')
info = {}
tag = soup.find_all(id='submission_status')[0]
info['status'] = tag.text.strip()
tags = soup.find_all(id='compilation')
if tags:
content = tags[0]
info['compile_output'] = None
info['compile_output'] = '\n'.join([pre.text.strip() for pre in content.
    findAll('pre')])
evaluations = []
tags = soup.find_all(id=re.compile('^eval_outcome_'))
text_tags = soup.find_all(id=re.compile('^eval_text_'))
for outcome_tag, text_tag in zip(tags, text_tags):
evaluations.append({'outcome': outcome_tag.text.strip(), 'text': text_tag.
    text.strip()})
info['evaluations'] = evaluations
return info
