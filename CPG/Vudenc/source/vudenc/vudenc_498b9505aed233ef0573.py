from odoo import models
from odoo.addons.base_crapo_workflow.mixins import crapo_automata_mixins
"""
    Base class to define a Business Object.

    Should be use as a mixin class in existing objects
    """
_name = 'crapo.business.object'
_inherit = ['mail.thread', 'mail.activity.mixin']
_description = """
    An object on which to  in a workflow, specific to a given model
    """
_sync_state_field = ''
