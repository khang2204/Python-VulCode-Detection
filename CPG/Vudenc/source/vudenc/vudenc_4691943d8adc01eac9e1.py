def __iter__(self) ->Iterator[IRow]:...
spy = Spy()
yield spy
query_string = construct_select_statement(spy, self.from_object)
print(query_string)
yield from self.client.query(query_string)
