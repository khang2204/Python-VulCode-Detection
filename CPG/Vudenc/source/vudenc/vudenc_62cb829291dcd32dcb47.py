import logging
import tempfile
import uuid
from odoo import api, registry, fields, models, _
from odoo.tools import mod10r
from odoo.tools.config import config
from odoo.addons.base_geoengine.fields import GeoPoint
from odoo.addons.base_geoengine import fields as geo_fields
ADDRESS_FIELDS = ['street', 'street2', 'street3', 'zip', 'city', 'state_id',
    'country_id']
logger = logging.getLogger(__name__)
import pyminizip
logger.warning('Please install python dependencies.', exc_info=True)
""" This class upgrade the partners to match Compassion needs.
        It also synchronize all changes with the MySQL server of GP.
    """
import csv
_inherit = 'res.partner'
from smb.SMBConnection import SMBConnection
def _get_receipt_types(self):...
from smb.smb_structs import OperationFailure
"""docstring"""
return [('no', _('No receipt')), ('default', _('Default')), ('only_email',
    _('Only email')), ('paper', _('On paper'))]
