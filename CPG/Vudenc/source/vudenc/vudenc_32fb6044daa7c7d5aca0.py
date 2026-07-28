@api.multi...
for lead in self:
lead.phonecall_count = self.env['crm.phonecall'].search_count([(
    'opportunity_id', '=', lead.id)])
