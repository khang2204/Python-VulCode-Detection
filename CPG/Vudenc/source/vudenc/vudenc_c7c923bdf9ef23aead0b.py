def finish(self):...
if not self.final:
start = self.marks[0][1]
return self.final
end = time.time() if len(self.marks) == 1 else self.marks[-1][1]
diff_ms = lambda start, end: int((end - start) * 1000)
durations = [(name, diff_ms(self.marks[i][1], ts)) for i, (name, ts) in
    enumerate(self.marks[1:])]
self.final = {'timestamp': int(start), 'duration_ms': diff_ms(start, end),
    'marks_ms': {key: sum(d[1] for d in group) for key, group in groupby(
    sorted(durations), key=lambda x: x[0])}}
