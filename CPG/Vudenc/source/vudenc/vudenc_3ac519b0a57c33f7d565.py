@_transform.route('/find_and_replace', methods=['POST'])...
dataset = get_dataset_with_id(request.args.get('dataset_id'))
col = request.form['column']
find = request.form['find']
match_mode = request.form['match-mode']
replace = request.form['replace']
if match_mode == 'full-match':
find_replace(dataset.working_copy, col, find, replace)
if match_mode == 'substring-match':
return redirect(request.referrer)
replace_mode = request.form['replace-mode']
if match_mode == 'regex-match':
if replace_mode == 'full-replace':
regex_find_replace(dataset.working_copy, col, find, replace)
substring_find_replace(dataset.working_copy, col, find, replace, full=True)
if replace_mode == 'substring-replace':
substring_find_replace(dataset.working_copy, col, find, replace, full=False)
