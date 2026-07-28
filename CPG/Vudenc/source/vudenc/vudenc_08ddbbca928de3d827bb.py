def output_json(points, deductions):...
score = points - sum(d['points'] for d in deductions)
if score < 0:
score = 0
print(json.dumps({'score': score, 'deductions': deductions}))
