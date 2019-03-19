# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteBlogPostRightColumn(http.Controller):
#     @http.route('/website_blog_post_right_column/website_blog_post_right_column/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_blog_post_right_column/website_blog_post_right_column/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_blog_post_right_column.listing', {
#             'root': '/website_blog_post_right_column/website_blog_post_right_column',
#             'objects': http.request.env['website_blog_post_right_column.website_blog_post_right_column'].search([]),
#         })

#     @http.route('/website_blog_post_right_column/website_blog_post_right_column/objects/<model("website_blog_post_right_column.website_blog_post_right_column"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_blog_post_right_column.object', {
#             'object': obj
#         })