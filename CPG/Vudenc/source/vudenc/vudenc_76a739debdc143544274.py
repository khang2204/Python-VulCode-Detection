def _from(self):...
from_str = """
        qc_problem qcp
            left join helpdesk_problem_rel hpr on hpr.qc_problem_id = qcp.id
            left join crm_helpdesk chd on chd.id = hpr.crm_helpdesk_id
        """
return from_str
