# -*- coding: utf-8 -*-
# License MIT #

from odoo import api, fields, models, tools

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    floating_whatsapp_id = fields.Many2one(related="website_id.floating_whatsapp_id")