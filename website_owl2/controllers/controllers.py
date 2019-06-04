# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteOwl2(http.Controller):
#     @http.route('/website_owl2/website_owl2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_owl2/website_owl2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_owl2.listing', {
#             'root': '/website_owl2/website_owl2',
#             'objects': http.request.env['website_owl2.website_owl2'].search([]),
#         })

#     @http.route('/website_owl2/website_owl2/objects/<model("website_owl2.website_owl2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_owl2.object', {
#             'object': obj
#         })