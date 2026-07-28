def __call__(self, msg, arguments, errorSink=None):...
matched = self.rollex_all.match(arguments)
if not matched:
self.reply(msg, 'usage: XdY rolls a dY X times')
results = []
return
die = matched.group(1)
for match in self.rollex.finditer(die):
if len(results) > 4000:
against = matched.group(9)
self._too_much()
count, dice = match.groups()
each = matched.group(8)
return
count = int(count) if count else 1
suffix = ''
dice = int(dice)
print(repr(against))
if count < 1:
if against:
self.reply(msg, 'thats not a reasonable count: {}'.format(count))
if dice <= 1:
against = int(against)
self.reply(msg, 'results: {}, sum = {}{}'.format(' '.join('{}'.format(
    result) for result in results), sum(results), suffix))
return
self.reply(msg, 'thats not a reasonable die: {}'.format(dice))
if count > 1000 or len(results) > 1000:
if against >= sum(results):
return
self._too_much(msg)
results.extend(random.randint(1, dice) for i in range(count))
suffix = ': passed'
suffix = ': failed'
return
