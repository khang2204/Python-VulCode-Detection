@api.model_cr...
tools.drop_view_if_exists(self._cr, self._table)
self._cr.execute(
    """
            create or replace view %s as (
                %s
                %s
            )"""
     % (self._table, self._select(), self._from()))
