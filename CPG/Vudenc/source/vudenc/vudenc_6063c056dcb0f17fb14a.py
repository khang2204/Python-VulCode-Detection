def generate_graphviz_plot(self):...
def run_status(obj):...
if obj.do_not_run is True:
s = 'DNR'
s = 'RUN'
s += '_{}'.format(obj.id)
return s
