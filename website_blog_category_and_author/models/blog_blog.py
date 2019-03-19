# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import models, fields, api, _


class Blog(models.Model):
    _inherit = ['blog.blog']

    website_category_ids = fields.One2many(string='Website Categories', comodel_name='blog.category',inverse_name='blog_id')
