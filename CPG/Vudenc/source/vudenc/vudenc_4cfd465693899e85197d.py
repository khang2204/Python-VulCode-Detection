def _select(self):...
select_str = """
             SELECT qcp.id as id,
                    qcp.name as name,
                    qcp.notes as notes,
                    qcp.problem_group_id as problem_group_id,
                    qcp.color as color,
                    qcp.priority as priority,
                    qcp.stage_id as stage_id,
                    qcp.qc_team_id as qc_team_id,
                    qcp.company_id as company_id,
                    count(hpr) as crm_helpdesk_count,
                    chd.date as date
        """
return select_str
