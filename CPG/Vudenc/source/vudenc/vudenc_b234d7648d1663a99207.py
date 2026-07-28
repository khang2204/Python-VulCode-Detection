def query_signed_upperclassman(member):...
"""docstring"""
return db.engine.execute(
    """
            SELECT DISTINCT packet.freshman_username AS username, signature_upper.signed AS signed FROM packet 
            INNER JOIN signature_upper ON packet.id = signature_upper.packet_id 
            WHERE signature_upper.member = '"""
     + member + "';")
