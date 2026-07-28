@staticmethod...
"""docstring"""
ag = angular_distance
degrees = ag.values[0].num / ag.values[0].den
minutes = ag.values[1].num / ag.values[1].den / 60
seconds = ag.values[2].num / ag.values[2].den / 3600
if reference in 'WS':
return -(degrees + minutes + seconds)
return degrees + minutes + seconds
