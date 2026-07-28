def query_signed_alumni(member):...
"""docstring"""
return db.engine.execute(
    """
            SELECT DISTINCT packet.freshman_username AS username, signature_misc.member AS signed 
            FROM packet LEFT OUTER JOIN signature_misc ON packet.id = signature_misc.packet_id 
            WHERE signature_misc.member = '"""
     + member + "' OR signature_misc.member ISNULL;")
