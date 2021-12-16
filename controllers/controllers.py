# -*- coding: utf-8 -*-
# from odoo import http


# class Validations(http.Controller):
#     @http.route('/validations/validations/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/validations/validations/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('validations.listing', {
#             'root': '/validations/validations',
#             'objects': http.request.env['validations.validations'].search([]),
#         })

#     @http.route('/validations/validations/objects/<model("validations.validations"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('validations.object', {
#             'object': obj
#         })
