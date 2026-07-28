from collections import namedtuple
from logging import getLogger
from sqlalchemy import exc
from .models import db, REQUIRED_MISC_SIGNATURES
from .packet import get_number_required, get_misc_signatures
LOGGER = getLogger(__name__)
def current_packets(member, intro=False, onfloor=False):...
"""docstring"""
SPacket = namedtuple('spacket', ['rit_username', 'name', 'did_sign',
    'total_signatures', 'required_signatures'])
packets = []
required = get_number_required()
if intro and onfloor:
required -= 1
signed_packets = get_signed_packets(member, intro, onfloor)
misc_signatures = get_misc_signatures()
for pkt in query_packets_with_signed():
LOGGER.error(e)
return packets
signed = signed_packets.get(pkt.username)
misc = misc_signatures.get(pkt.username)
if signed is None:
signed = False
if misc is None:
misc = 0
if misc > REQUIRED_MISC_SIGNATURES:
misc = REQUIRED_MISC_SIGNATURES
packets.append(SPacket(pkt.username, pkt.name, signed, pkt.received + misc,
    required))
