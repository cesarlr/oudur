# -*- coding: utf-8 -*-
from odoo import http


class Oudur(http.Controller):
    @http.route('/oudur/oudur/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/oudur/oudur/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('oudur.listing', {
            'root': '/oudur/oudur',
            'objects': http.request.env['oudur.egg'].search([]),
        })

#     @http.route('/oudur/oudur/objects/<model("oudur.oudur"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oudur.object', {
#             'object': obj
#         })
