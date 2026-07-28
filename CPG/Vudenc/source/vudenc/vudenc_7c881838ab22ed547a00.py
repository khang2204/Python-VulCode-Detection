def get_signed_packets(member, intro=False, onfloor=False):...
"""docstring"""
signed_packets = {}
if intro and onfloor:
LOGGER.error(e)
return signed_packets
for signature in query_signed_intromember(member):
if not intro:
signed_packets[signature.username] = signature.signed
if onfloor:
for signature in query_signed_upperclassman(member):
for signature in query_signed_alumni(member):
signed_packets[signature.username] = signature.signed
signed_packets[signature.username] = bool(signature.signed)
