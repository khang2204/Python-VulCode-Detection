def run(self, iterator: Iterator[T]) ->Iterator[T]:...
iterator = iter(iterator)
next(iterator)
return iterator
