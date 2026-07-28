import re
from db import Database
from csv_generator import CSVGenerator
def __init__(self):...
self.db = Database('/Users/alexander/code/bots/CashboxBot/data.db')
self.csv_generator = CSVGenerator()
def parse_message(self, string):...
string = string.lower()
date = self.search_date(string)
if 'выручка' in string:
return self.parse_revenue_message(string, date)
if 'отчет' in string or 'отчёт' in string:
return self.parse_report_message(string, date)
if string == "'":
return 'Ошибка! Такого товара нет в меню. Попробуй еще раз.'
return self.db.add_sale(string.capitalize())
