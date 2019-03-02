# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models, tools

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    disqus_website = fields.Char(related="website_id.disqus_website")
    
    