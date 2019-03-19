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
    'version': '12.0.0.0.0',

  
    'depends': ['base_automation', 'website_blog'],

 
    'data': [
        'views/website_blog_views.xml',
        'views/templates.xml',
        'data/blog_post.xml',
    ],
     'license': 'AGPL-3',
}