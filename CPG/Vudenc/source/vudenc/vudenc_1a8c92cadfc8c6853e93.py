def __exit__(self, type, value, traceback):...
transaction = self._transactions.pop()
if type is None:
transaction.commit()
transaction.rollback()
