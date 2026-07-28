@staticmethod...
"""docstring"""
query = (
    """SELECT mapped_by as contributors from tasks where project_id = {0} and  mapped_by is not null
                   UNION
                   SELECT validated_by from tasks where tasks.project_id = {0} and validated_by is not null"""
    .format(project_id))
contributors = db.engine.execute(query)
return contributors
