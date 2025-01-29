# -*- coding: utf-8 -*-

from odoo import models, fields


class CustomProduct(models.Model):
    _name = 'custom.product'
    _description = 'Custom Product'

    name = fields.Char(string="Product Name", required=True)
    description = fields.Text(string="Description")
    price = fields.Float(string="Price", required=True)
    image = fields.Binary(string="Image")
    is_published = fields.Boolean(string="Publish on Website", default=True)

class CustomRFQ(models.Model):
    _name = 'custom.rfq'
    _description = 'Request for Quotation'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    contact = fields.Char(string='Contact')
    quantity = fields.Integer(string='Quantity', required=True)
    description = fields.Text(string='Description')
    product_id = fields.Many2one('custom.product', string='Product', required=True)  # if associated with a product
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('processed', 'Processed'),
    ], default='draft', string='Status')
