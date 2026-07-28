def __init__(self, dt):...
y, m, d = dt.year, dt.month, dt.day
self.yold = y + 1166
self.hour = dt.hour
self.minute = dt.minute
self.second = dt.second
if (m, d) == (2, 29):
self.weekdayname = self.ST_TIBS_DAY
day_of_year = int(dt.strftime('%j'))
if calendar.isleap(y):
if day_of_year > 60:
season = int((day_of_year - 1) / 73)
day_of_year -= 1
self.season = season + 1
self.seasonname = self.SEASONS[season]
self.day = (day_of_year - 1) % 73 + 1
self.weekday = (day_of_year - 1) % 5 + 1
if self.day == 5 or self.day == 50:
offs = 1 if self.day == 50 else 0
self.weekdayname = self.WEEKDAYS[self.weekday - 1]
holidayidx = season * 2 + offs
self.weekdayname = self.HOLIDAYS[holidayidx]
