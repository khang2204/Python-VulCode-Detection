from openerp import api, models, fields
import logging
from datetime import datetime, timedelta
_logger = logging.getLogger(__name__)
_inherit = 'product.template'
item_code = fields.Char(help='Code from bulonfer, not shown', select=1)
upv = fields.Integer(help='Group Wholesaler')
wholesaler_bulk = fields.Integer(help='Bulk Wholesaler quantity of units')
retail_bulk = fields.Integer(help='Bulk retail quantity of units')
invalidate_category = fields.Boolean(help=
    'True if the asociated category needs rebuild', default=False)
system_cost = fields.Float(help='Cost price based on the purchase invoice')
margin = fields.Float(help='Margin % from today cost to list price')
bulonfer_cost = fields.Float(help=
    """Today cost in product currency, it is automatically updated when the prices coming from Bulonfer are processed.
Or when a price sheet is loaded for no Bulonfer vendors"""
    )
cost_history_ids = fields.One2many(comodel_name='stock.quant', inverse_name
    ='product_tmpl_id', domain=[('location_id.usage', '=', 'internal')])
parent_price_product = fields.Char(help=
    'default_code of the product to get prices from')
def oldest_quant(self, prod):...
"""docstring"""
quant_obj = self.env['stock.quant']
return quant_obj.search([('product_tmpl_id', '=', prod.id), (
    'location_id.usage', '=', 'internal')], order='in_date', limit=1)
