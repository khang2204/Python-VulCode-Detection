def _read_group_states(self, states, domain, order):...
search_domain = self._get_state_domain(domain=domain)
state_ids = states._search(search_domain, order=order, access_rights_uid=
    SUPERUSER_ID)
return states.browse(state_ids)
