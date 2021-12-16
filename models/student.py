# -*- coding: utf-8 -*-

from odoo import models, fields, api
from random import choice

class student(models.Model):
    _name = 'validations.student'
    _description = 'Student model'

    name = fields.Char(String = "Name", required = True, index = True)
    password = fields.Char(String = "Password", required = False, index = True, default = "")
    photo = fields.Binary()
    age = fields.Integer(String = "Age", required = True, index = True)
    city = fields.Char(String = "City", required = True, index = True)
    province = fields.Char(String = "Province", required = True, index = True)
    mail = fields.Char(String = "mail", required = True, index = True)

    convalidation = fields.One2many("validations.convalidation", "module", String = "Convalidations")

    def generate_password(self):
        self.ensure_one()
        size = 10
        values = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        p = ""
        p = p.join([choice(values) for i in range(size)])
        self.password = p
        return True
