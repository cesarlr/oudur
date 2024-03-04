# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Egg(models.Model):
     _name = 'oudur.egg'
     _description = 'Date, size and other info about the boiled egg'

     harvest_date = fields.Date('Harvest Date', default=fields.Date.today())
     serial_number = fields.Char('Serial Number', size=12, default=lambda self: self._get_sequence())
     state = fields.Selection([('fresh', 'Fresh'), ('poached', 'Poached'), ('hard', 'Hard')], 'State')

     def _get_sequence(self):
        return self.env['ir.sequence'].next_by_code('egg.serial')
