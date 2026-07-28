def build_and_run(self):...
args = self.prepare_args()
args.limit = self.add_limit()
if args.conditions:
args.conditions = 'where ' + args.conditions
if self.distinct:
args.fields = 'distinct ' + args.fields
query = (
    """select %(fields)s from %(tables)s %(conditions)s
			%(group_by)s %(order_by)s %(limit)s"""
     % args)
return frappe.db.sql(query, as_dict=not self.as_list, debug=self.debug,
    update=self.update)
