def print_top_errors():...
"""docstring"""
print('On which days did more than 1% of requests lead to errors?\n')
top_authors = '%s - % 6.2f%% errors\n'
results = ''.join(top_authors % (logdate, err_pct) for logdate, err_pct in
    get_most_error_day())
print(results)
