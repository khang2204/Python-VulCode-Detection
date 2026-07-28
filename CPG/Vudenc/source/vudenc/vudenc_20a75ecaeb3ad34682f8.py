def query_packets_with_signed():...
"""docstring"""
return db.engine.execute(
    """
        SELECT packets.username AS username, packets.name AS name, coalesce(packets.sigs_recvd, 0) AS received 
         FROM ( ( SELECT freshman.rit_username 
         AS username, freshman.name AS name, packet.id AS id, packet.start AS start, packet.end AS end 
         FROM freshman INNER JOIN packet ON freshman.rit_username = packet.freshman_username) AS a 
                       LEFT JOIN (  SELECT totals.id  AS id, coalesce(sum(totals.signed), 0)  AS sigs_recvd 
                       FROM ( SELECT packet.id AS id, coalesce(count(signature_fresh.signed), 0) AS signed 
                       FROM packet FULL OUTER JOIN signature_fresh ON signature_fresh.packet_id = packet.id 
                       WHERE signature_fresh.signed = TRUE  AND packet.start < now() AND now() < packet.end 
                       GROUP BY packet.id 
                       UNION SELECT packet.id AS id, coalesce(count(signature_upper.signed), 0) AS signed FROM packet 
                       FULL OUTER JOIN signature_upper ON signature_upper.packet_id = packet.id 
                       WHERE signature_upper.signed = TRUE AND packet.start < now() AND now() < packet.end 
                       GROUP BY packet.id ) totals GROUP BY totals.id ) AS b ON a.id = b.id ) AS packets 
                       WHERE packets.start < now() AND now() < packets.end; 
                                """
    )
