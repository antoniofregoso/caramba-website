# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
{
    'name': "Blog Post Right Column",

    'summary': 'Add new features to the blog',

    'description': """
Advanced management of post presentation in blogs.
======================================

Key Features
------------
* Right column.
* Most read posts with and without image.
* Post related with and without image.
* Customizing the lists of posts.
* Creative Commons.
""",

    'author': "Antonio Fregoso",
    'website': "http://www.antoniofregoso.blog",
    'category': 'Website',
    'version': '11.0.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base_automation', 'website_blog', 'website_unitegallery'],

    # always loaded
    'data': [
        'views/website_blog_views.xml',
        'views/templates.xml',
        'data/blog_post.xml',
    ],
     'license': 'AGPL-3',
}
