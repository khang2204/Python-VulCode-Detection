def prepare_args(self):...
self.parse_args()
self.sanitize_fields()
self.extract_tables()
self.set_optional_columns()
self.build_conditions()
args = frappe._dict()
if self.with_childnames:
for t in self.tables:
args.tables = self.tables[0]
if t != '`tab' + self.doctype + '`':
for child in self.tables[1:]:
self.fields.append(t + ".name as '%s:name'" % t[4:-1])
args.tables += ' {join} {child} on ({child}.parent = {main}.name)'.format(join
    =self.join, child=child, main=self.tables[0])
if self.grouped_or_conditions:
self.conditions.append('({0})'.format(' or '.join(self.grouped_or_conditions)))
args.conditions = ' and '.join(self.conditions)
if self.or_conditions:
args.conditions += (' or ' if args.conditions else '') + ' or '.join(self.
    or_conditions)
self.set_field_tables()
args.fields = ', '.join(self.fields)
self.set_order_by(args)
self.validate_order_by_and_group_by(args.order_by)
args.order_by = args.order_by and ' order by ' + args.order_by or ''
self.validate_order_by_and_group_by(self.group_by)
args.group_by = self.group_by and ' group by ' + self.group_by or ''
return args
