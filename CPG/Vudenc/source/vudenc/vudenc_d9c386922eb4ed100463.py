def read_data(self, sensors=None):...
"""docstring"""
if sensors is None:
sensors = self.sensors
for i, _ in enumerate(sensors):
if random() < 0.01:
yield 'NULL'
value = gauss(293 + 0.5 * i, 0.1)
yield f'{value:.4f}'
