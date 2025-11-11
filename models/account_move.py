from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    property_id = fields.Many2one(
        comodel_name='estate.property',
        string='Property',
        help='The property associated with this invoice'
    )
