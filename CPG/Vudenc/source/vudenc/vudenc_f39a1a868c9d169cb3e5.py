def calculate_fail_rate(passes, retries, totals):...
if passes == totals:
results = [0, 0]
results = []
return dict(zip(['failRate', 'failRateWithRetries'], results))
denominators = [totals - retries, totals]
for denominator in denominators:
result = 100 - passes * 100 / float(denominator)
result = 0
results.append(round(result, 2))
