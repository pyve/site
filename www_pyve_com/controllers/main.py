# -*- coding: utf-8 -*-

# class WwwPyveCom(http.Controller):
#     @http.route('/www_pyve_com/www_pyve_com/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/www_pyve_com/www_pyve_com/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('www_pyve_com.listing', {
#             'root': '/www_pyve_com/www_pyve_com',
#             'objects': http.request.env[
#                   'www_pyve_com.www_pyve_com'].search([]),
#         })

#     @http.route('/www_pyve_com/www_pyve_com/objects/<model("www_pyve_com.www_pyve_com"):obj>/', auth='public')  # noqa
#     def object(self, obj, **kw):
#         return http.request.render('www_pyve_com.object', {
#             'object': obj
#         })
