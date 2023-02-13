# -*- coding: utf-8 -*-
from odoo import fields,models

class ShowtimeTickets(models.Model):
    _name="showtime.tickets"
    _description="ShowTime Tickets Description"

    name = fields.Char(required=True)
    price = fields.Integer(required=True)
    max_qty = fields.Integer(required=True,default=200)
    current_qty = fields.Integer(required=True,default=0)
    show_id = fields.Many2one("showtime.shows")