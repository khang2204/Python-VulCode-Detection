def days_interval_to_text(interval_list):...
result = ['< 1 day', '1 day']
for i in interval_list[2:-1]:
result.append(f'{i.left}-{i.right - 1 if i.open_right else i.right} days')
result = result + ['90+ days']
return result
