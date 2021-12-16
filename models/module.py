# -*- coding: utf-8 -*-

from odoo import models, fields, api


class module(models.Model):
    _name = 'validations.module'
    _description = 'Module model'

    name = fields.Char(String = "Name", required = True)
    description = fields.Text(required = True)
    hours = fields.Integer(String = "Hours", required = True)
    vt = fields.Many2one("validations.vocationaltraining", String = "VTs")
