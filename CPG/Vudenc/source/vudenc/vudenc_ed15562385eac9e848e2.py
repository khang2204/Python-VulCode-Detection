import odin
from odin.fields.virtual import CalculatedField
from odin.mapping.helpers import sum_fields
name = odin.StringField()
name_space = None
name = odin.StringField()
name_space = None
abstract = True
name_space = 'library'
key_field = 'isbn'
title = odin.StringField()
isbn = odin.StringField()
num_pages = odin.IntegerField()
rrp = odin.FloatField(default=20.4, use_default_if_not_provided=True)
fiction = odin.BooleanField(is_attribute=True)
genre = odin.StringField(choices=(('sci-fi', 'Science Fiction'), ('fantasy',
    'Fantasy'), ('biography', 'Biography'), ('others', 'Others'), (
    'computers-and-tech', 'Computers & technology')))
published = odin.TypedArrayField(odin.DateTimeField())
authors = odin.ArrayOf(Author, use_container=True)
publisher = odin.DictAs(Publisher, null=True)
def __eq__(self, other):...
if other:
return vars(self) == vars(other)
return False
