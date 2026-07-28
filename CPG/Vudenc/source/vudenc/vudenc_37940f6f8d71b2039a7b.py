@api.model_cr...
tools.drop_view_if_exists(self.env.cr, self._table)
self.env.cr.execute(
    """CREATE or REPLACE VIEW %s as (
            %s
            FROM ( %s )
            %s
            )"""
     % (self._table, self._select(), self._from(), self._group_by()))
