from typing import Iterator, TypeVar
from .construct import construct_select_statement
from .interface import IRow
from .spy import Spy
T = TypeVar('T')
def __init__(self, from_object: str, client):...
self.from_object = from_object
self.client = client
def run(self, iterator: Iterator[T]) ->Iterator[T]:...
iterator = iter(iterator)
next(iterator)
return iterator
