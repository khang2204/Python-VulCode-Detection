def query_signed_intromember(member):...
"""docstring"""
return db.engine.execute(
    """
            SELECT DISTINCT packet.freshman_username AS username, signature_fresh.signed AS signed FROM packet 
            INNER JOIN signature_fresh ON packet.id = signature_fresh.packet_id 
            WHERE signature_fresh.freshman_username = '"""
     + member + "';")
