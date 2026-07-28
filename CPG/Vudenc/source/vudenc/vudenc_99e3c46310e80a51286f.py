def save_targets(self):...
data = {'targets': targets, 'forums': forums, 'domains': domains, 'sets':
    self.pc.sets}
f.write(pickle.dumps(data, pickle.HIGHEST_PROTOCOL))
