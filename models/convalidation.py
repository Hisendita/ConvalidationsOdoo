# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class convalidation(models.Model):
    _name = 'validations.convalidation'
    _description = 'Convalidation model'

    date = fields.Date(String="Date", required=True, default=datetime.today())
    module = fields.Many2one("validations.module", String="Module") 
    student = fields.Many2one("validations.student", String="Student")