# -*- coding: utf-8 -*-
{
    'name': "Website Blog Category And Author",

    'summary': "",
    'description': "",

    'author': "Antonio Fregoso",
    'website': "http://www.antoniofregoso.blog",
    'category': 'Website',
    'version': '11.0.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['website_blog_post_right_column', 'web_widget_color', ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/blog_category_view.xml',
        'views/blog_views.xml',
        'views/res_partner_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/blog_category_demo.xml',
    ],
    'license': 'AGPL-3',
}
