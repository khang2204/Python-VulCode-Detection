def parse_revenue_message(self, string, date):...
if date and self.db.check_date(date):
return self.db.revenue(date)
if date:
return 'Нет данных за этот день.'
if string == 'выручка':
return self.db.revenue()
return 'Ошибка! Неверный формат даты.'
