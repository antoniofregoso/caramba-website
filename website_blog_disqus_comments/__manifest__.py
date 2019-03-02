# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
{
    'name': "Blog Post Disqus Comments",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",


    'author': "Antonio Fregoso",
    'website': "http://www.antoniofregoso.blog",
    'category': 'Website',
    'version': '11.0.0.0.0',
    'depends': ['website_blog_post_right_column'],


    'data': [
        'views/res_config_settings.xml',
        'views/templates.xml',
    ],
    
    
    'license': 'AGPL-3',
}