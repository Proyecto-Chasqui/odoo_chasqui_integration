from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    external_sale_ok = fields.Boolean(string='Can be Sold on Chasqui')
    external_product_id = fields.Char(string='Chasqui Product ID')
    sync_id = fields.Char(string='Sync ID')
    sync_hash = fields.Char(string='Sync Hash')
    sync_timestamp = fields.Datetime(string='Last Sync Timestamp')
