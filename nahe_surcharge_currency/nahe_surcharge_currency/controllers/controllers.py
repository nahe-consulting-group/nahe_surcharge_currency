# -*- coding: utf-8 -*-
# from odoo import http


# class NaheSurchargeCurrency(http.Controller):
#     @http.route('/nahe_surcharge_currency/nahe_surcharge_currency/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nahe_surcharge_currency/nahe_surcharge_currency/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nahe_surcharge_currency.listing', {
#             'root': '/nahe_surcharge_currency/nahe_surcharge_currency',
#             'objects': http.request.env['nahe_surcharge_currency.nahe_surcharge_currency'].search([]),
#         })

#     @http.route('/nahe_surcharge_currency/nahe_surcharge_currency/objects/<model("nahe_surcharge_currency.nahe_surcharge_currency"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nahe_surcharge_currency.object', {
#             'object': obj
#         })
