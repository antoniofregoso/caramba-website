# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#


from odoo import models, fields, api, _

class BlogPost(models.Model):

    _inherit = 'blog.post'


    website_category_id = fields.Many2one(
        string='Website Category',
        comodel_name='blog.category',
    )

    @api.model
    def search(self, domain, *args, **kwargs):
        if self.env.context.get('search_category_id'):
            category = self.env.context['search_category_id']
            domain += [
                ('website_category_id', 'child_of', category),
            ]
        return super(BlogPost, self).search(domain, *args, **kwargs)
