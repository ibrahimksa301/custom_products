# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class CustomProductWebsite(http.Controller):

    @http.route('/custom-products', type='http', auth='public', website=True)
    def list_custom_products(self, **kwargs):
        products = request.env['custom.product'].sudo().search([('is_published', '=', True)])
        return request.render('custom_products.template_custom_products', {'products': products})

    @http.route('/product/<int:product_id>', type='http', auth='public', website=True)
    def product_details(self, product_id):
        product = request.env['custom.product'].sudo().browse(product_id)
        if not product.exists():
            return request.not_found()
        return request.render('custom_products.template_product_details', {'product': product})


# class CustomRFQController(http.Controller):
#
#     # Route to display the RFQ form for a specific product
#     @http.route('/product/rfq/<int:product_id>', type='http', auth='public', website=True)
#     def rfq_form(self, product_id, **kwargs):
#         # Get the product from custom.product model
#         product = request.env['custom.product'].browse(product_id)
#
#         if not product.exists():
#             return request.not_found()  # If the product doesn't exist, show a 404 page
#
#         return request.render('custom_products.template_rfq_form', {'product': product})
#
#     # Route to handle the RFQ form submission and create a new RFQ record
#     @http.route('/submit-rfq/<int:product_id>', type='http', auth='public', methods=['POST'], website=True)
#     def submit_rfq(self, product_id, **post):
#         # Get the form data from the POST request
#         name = post.get('name')
#         email = post.get('email')
#         contact = post.get('contact')
#         quantity = post.get('quantity')
#         description = post.get('description')
#
#         if not all([name, email, quantity]):
#             # Handle missing data error
#             return request.render("custom_products.error_page")
#
#         # Create a new RFQ record in the backend
#         rfq = request.env['custom.rfq'].sudo().create({
#             'name': name,
#             'email': email,
#             'contact': contact,
#             'quantity': quantity,
#             'description': description,
#             'product_id': product_id,
#             'state': 'draft',  # RFQ initially created as 'draft'
#         })
#
#         # Redirect to a "Thank You" page after form submission
#         return request.render('custom_products.thank_you_template', {'rfq': rfq})
