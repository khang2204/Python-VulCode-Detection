def __call__(self, msg, arguments, errorSink=None):...
if arguments.strip():
return
current_date = date.today()
current_cw = current_date.isocalendar()[1]
current_year = current_date.year
paritystr = ''
if current_cw % 2 == 0:
paritystr = 'even'
paritystr = 'odd'
self.reply(msg, 'Current week is week #{cw} in {year}, which is {parity}.'.
    format(cw=current_cw, year=current_year, parity=paritystr))
