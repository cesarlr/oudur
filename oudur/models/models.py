# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Egg(models.Model):
    _name = 'oudur.egg'
    _description = 'Date, size and other info about the boiled egg'

    harvest_date = fields.Date('Harvest Date', default=fields.Date.today())
    serial_number = fields.Char(
            'Serial Number',
            size=12,
            default=lambda self: self._get_sequence()
    )
    state = fields.Selection(
            [('fresh', 'Fresh'), ('poached', 'Poached'), ('hard', 'Hard')],
            'State', compute='_get_state'
    )
    size = fields.Selection([('m','M'),('l','L'),('xl','XL')], 'Size')
    cooking_time = fields.Integer('Cooking Time')

    def _get_sequence(self):
       return self.env['ir.sequence'].next_by_code('egg.serial')
    
    def _get_state(self):
        for egg in self:
            if egg.size == 'm':
                if egg.cooking_time < 2:
                    egg.state = 'fresh'
                elif egg.cooking_time <= 6:
                    egg.state = 'poached'
                else:
                    egg.state = 'hard'
            elif egg.size == 'l':
                if egg.cooking_time < 3:
                    egg.state = 'fresh'
                elif egg.cooking_time <= 7:
                    egg.state = 'poached'
                else:
                    egg.state = 'hard'
            else:
                if egg.cooking_time < 5:
                    egg.state = 'fresh'
                elif egg.cooking_time <= 9:
                    egg.state = 'poached'
                else:
                    egg.state = 'hard'
