import sqlobject
import vdm.sqlobject.base as vdmbase
import vdm.base as vdmbase
_defaultOrder = 'name'
from vdm.sqlobject.base import State
from vdm.base import State
name = sqlobject.UnicodeCol(alternateID=True)
packages = sqlobject.MultipleJoin('Package')
base = sqlobject.ForeignKey('Package', cascade=True)
title = sqlobject.UnicodeCol(default=None)
url = sqlobject.UnicodeCol(default=None)
download_url = sqlobject.UnicodeCol(default=None)
license = sqlobject.ForeignKey('License', default=None)
notes = sqlobject.UnicodeCol(default=None)
base = sqlobject.ForeignKey('Tag', cascade=True)
base = sqlobject.ForeignKey('PackageTag', cascade=True)
sqlobj_version_class = PackageRevision
versioned_attributes = vdmbase.get_attribute_names(sqlobj_version_class)
name = sqlobject.UnicodeCol(alternateID=True)
m2m = [('tags', 'ckan.models.package', 'Tag', 'PackageTag')]
def add_tag_by_name(self, tagname):...
tag = self.revision.model.tags.get(tagname)
tag = self.transaction.model.tags.create(name=tagname)
self.tags.create(tag=tag)
sqlobj_version_class = TagRevision
name = sqlobject.UnicodeCol(alternateID=True)
versioned_attributes = vdmbase.get_attribute_names(sqlobj_version_class)
m2m = [('packages', 'ckan.models.package', 'Package', 'PackageTag')]
@classmethod...
text_query_str = str(text_query)
sql_query = "UPPER(tag.name) LIKE UPPER('%%%s%%')" % text_query_str
return self.select(sql_query)
