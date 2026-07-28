def parse_report_message(self, string, date):...
if date and self.db.check_date(date):
return self.csv_generator.write_csv(date)
if date:
return 'Нет данных за этот день.'
if string == 'отчет' or string == 'отчёт':
return self.csv_generator.write_csv()
return 'Ошибка! Неверный формат даты.'
