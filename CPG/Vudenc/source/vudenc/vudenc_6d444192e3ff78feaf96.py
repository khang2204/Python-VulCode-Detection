from typing import Iterator, TypeVar
from .interface import ISpy
T = TypeVar('T')
def construct_select_statement(spy: ISpy, from_: str) ->str:...
return f"SELECT {', '.join(construct_selects(spy))} FROM {from_}"
