from lxml import etree
from mx import DateTime
from mx.DateTime import now
import time
from tools.translate import _
from osv import fields, osv
from tools.translate import _
_name = 'project.project'
_description = 'Project'
def _complete_name(self, cr, uid, ids, name, args, context):...
res = {}
for m in self.browse(cr, uid, ids, context=context):
res[m.id] = (m.parent_id and m.parent_id.name + '/' or '') + m.name
return res
