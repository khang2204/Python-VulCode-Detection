from dataclasses import dataclass
from typing import Optional, List, Union, Any, Tuple
from . import db
note_id: Optional[int]
user_id: int
content: str
created_at: Optional[str] = None
updated_at: Optional[str] = None
def __json__(self, *args):...
return vars(self)
