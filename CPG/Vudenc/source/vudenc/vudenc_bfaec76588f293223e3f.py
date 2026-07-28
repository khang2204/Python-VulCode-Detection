def get(self, date):...
data = dict()
data['today'] = self.get_today()
data['requested'] = self.get_requested(date)
return data
