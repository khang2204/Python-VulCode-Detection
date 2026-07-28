@defer.inlineCallbacks...
res, _ = self.get('/mails', {'q': [query], 'w': [str(window)], 'p': [str(
    page)]})
res = yield res
defer.returnValue([ResponseMail(m) for m in res['mails']])
