from odoo import models, fields, api, Command
from odoo.exceptions import UserError


class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
        res = super(EstateProperty, self).action_sold()
        for rec in self:
            
            tax_name = 'IVA 16%'
            tax = self.env['account.tax'].search([('name', '=', tax_name)], limit=1)

            if not tax:
                tax = self.env['account.tax'].create({
                    'name': tax_name,
                    'amount_type': 'percent',
                    'amount': 16.0,
                    'type_tax_use': 'sale',
                })

            invoice = self.env['account.move'].create({
                'move_type': 'out_invoice',
                'partner_id': rec.buyer_id.id,
                'property_id': rec.id,
                'invoice_line_ids': [
                    Command.create({
                        'name': f'Sale of property {rec.name}',
                        'quantity': 1,
                        'price_unit': rec.selling_price,
                        'tax_ids': [(6, 0, [tax.id])],
                    }),
                    Command.create({
                        'name': 'Administrative Fee',
                        'quantity': 1,
                        'price_unit': 100.00,
                        'tax_ids': [(6, 0, [tax.id])],
                    }),
                ],
            })

            return {
                'type': 'ir.actions.act_window',
                'name': 'Invoice',
                'res_model': 'account.move',
                'view_mode': 'form',
                'res_id': invoice.id,
            }

        return res
