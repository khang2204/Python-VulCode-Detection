import stack.commands
from stack.exception import CommandError
"""
	Changes a string containing documention for an attribute

	<param type='string' name='attr' optional='0'>
	Name of the attribute
	</param>

	<param type='string' name='doc' optional='0'>
	Documentation of the attribute
	</param>
	
	<example cmd='set attr doc attr="ssh.use_dns" doc="hosts with ssh.use_dns == True will enable DNS lookups in sshd config."'>
	Sets the documentation string for 'ssh.use_dns'
	</example>

	<related>list attr doc</related>
	<related>set attr</related>
	"""
def run(self, params, args):...
attr, doc = self.fillParams([('attr', None, True), ('doc', None, True)])
rows = self.db.execute(
    """
			select attr from attributes where attr='%s'
			""" % attr)
if not rows:
self.db.execute("""
			delete from attributes_doc where attr='%s'
			""" % attr
    )
if doc:
self.db.execute(
    """
				insert into attributes_doc
				(attr, doc)
				values ('%s', '%s')
				"""
     % (attr, doc))
