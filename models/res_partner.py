from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    external_partner_id = fields.Char('Chasqui Partner ID')
    sync_id = fields.Char('Sync ID')
    sync_hash = fields.Char('Sync Hash')
    sync_timestamp = fields.Datetime('Last Sync Timestamp')