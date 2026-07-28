def get_transaction_from_kwargs(**kwargs):...
transaction_code = kwargs.get('transaction_code', None)
transaction = get_object_or_404(Transaction, code=transaction_code)
return transaction
