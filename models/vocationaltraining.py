# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vocationaltraining(models.Model):
    _name = 'validations.vocationaltraining'
    _description = 'Vocational Training model'

    name = fields.Char(String = "Name", required = True)
    description = fields.Text(required = True)
    modules = fields.One2many("validations.module", "name", String = "Modules")