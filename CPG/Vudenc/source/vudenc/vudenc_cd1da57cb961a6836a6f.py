def validate_not_using_analytics(page):...
"""docstring"""
analytics_scripts = ('ga.js', 'analytics.js', 'quant.js', 'chartbeat.js',
    'chartbeat_mab.js', 'beacon.js', 'krxd.net')
page_str = str(page.content)
for script in analytics_scripts:
if script in page_str:
return True
return False
