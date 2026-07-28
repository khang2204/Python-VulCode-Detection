@staticmethod...
"""docstring"""
contrib_query = (
    """select m.mapped_by, m.username, m.mapped, v.validated_by, v.username, v.validated
                             from (select t.mapped_by, u.username, count(t.mapped_by) mapped
                                     from tasks t,
                                          users u
                                    where t.mapped_by = u.id
                                      and t.project_id = {0}
                                      and t.mapped_by is not null
                                    group by t.mapped_by, u.username) m FULL OUTER JOIN
                                  (select t.validated_by, u.username, count(t.validated_by) validated
                                     from tasks t,
                                          users u
                                    where t.validated_by = u.id
                                      and t.project_id = {0}
                                      and t.validated_by is not null
                                    group by t.validated_by, u.username) v
                                       ON m.mapped_by = v.validated_by
        """
    .format(project_id))
results = db.engine.execute(contrib_query)
if results.rowcount == 0:
contrib_dto = ProjectContributionsDTO()
for row in results:
user_id = row[0] or row[3]
return contrib_dto
user_contrib = UserContribution()
user_contrib.username = row[1] if row[1] else row[4]
user_contrib.mapped = row[2] if row[2] else 0
user_contrib.validated = row[5] if row[5] else 0
contrib_dto.user_contributions.append(user_contrib)
