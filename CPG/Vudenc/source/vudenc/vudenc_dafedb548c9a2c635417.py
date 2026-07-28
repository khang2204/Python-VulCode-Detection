def get_magic_vars(self):...
results = {}
results['inventory_hostname'] = self.name
results['inventory_hostname_short'] = self.name.split('.')[0]
results['group_names'] = sorted([g.name for g in self.get_groups() if g.
    name != 'all'])
return results
