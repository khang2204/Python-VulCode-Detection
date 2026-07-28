def _format_date(self, dt):...
ddt = DiscordianDateTime(dt)
if ddt.day is None:
return 'Today is {weekdayname} in the YOLD {yold:04d}'.format(weekdayname=
    ddt.weekdayname, yold=ddt.yold)
return 'Today is {weekdayname}, the {card} day of {seasonname} in the YOLD {yold}'.format(
    weekdayname=ddt.weekdayname, card=self._cardinal_number(ddt.day),
    seasonname=ddt.seasonname, yold=ddt.yold)
