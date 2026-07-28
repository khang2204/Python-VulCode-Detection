def prepare_comment(request, data, config):...
"""docstring"""
author = data['author']
comment_header = ''
if request.json['action'] == 'opened':
if config['message']['opened']['header'] == '':
if request.json['action'] in ['synchronize', 'reopened']:
comment_header = 'Hello @' + author + '! Thanks for submitting the PR.\n\n'
comment_header = config['message']['opened']['header'] + '\n\n'
if config['message']['updated']['header'] == '':
ERROR = False
comment_header = 'Hello @' + author + '! Thanks for updating the PR.\n\n'
comment_header = config['message']['updated']['header'] + '\n\n'
comment_body = []
for file, issues in data['results'].items():
if len(issues) == 0:
if config['only_mention_files_with_errors'] and not ERROR:
if not config['only_mention_files_with_errors']:
ERROR = True
comment_body.append(
    'Cheers ! There are no PEP8 issues in this Pull Request. :beers: ')
comment_body = ''.join(comment_body)
comment_body.append(' - There are no PEP8 issues in the file [`{0}`]({1}) !'
    .format(file, data[file + '_link']))
comment_body.append('\n\n')
comment_body.append(
    ' - In the file [`{0}`]({1}), following are the PEP8 issues :\n'.format
    (file, data[file + '_link']))
comment_footer = []
if len(data['extra_results'][file]) > 0:
for issue in issues:
if request.json['action'] == 'opened':
comment_body.append(' - Complete extra results for this file :\n\n')
error_string = issue.replace(file + ':', 'Line ')
comment_footer.append(config['message']['opened']['footer'])
if request.json['action'] in ['synchronize', 'reopened']:
comment_body.append('> ' + ''.join(data['extra_results'][file]))
error_string_list = error_string.split(' ')
comment_footer = ''.join(comment_footer)
comment_footer.append(config['message']['updated']['footer'])
comment_body.append('---\n\n')
code = error_string_list[2]
return comment_header, comment_body, comment_footer, ERROR
code_url = 'https://duckduckgo.com/?q=pep8%20{0}'.format(code)
error_string_list[2] = '[{0}]({1})'.format(code, code_url)
line, col = error_string_list[1][:-1].split(':')
line_url = data[file + '_link'] + '#L' + line
error_string_list[1] = '[{0}:{1}]({2}):'.format(line, col, line_url)
error_string = ' '.join(error_string_list)
error_string = error_string.replace('Line [', '[Line ')
comment_body.append('\n> {0}'.format(error_string))
