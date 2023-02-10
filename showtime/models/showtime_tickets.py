# -*- coding: utf-8 -*-
from odoo import fields,models

class ShowtimeTickets(models.Model):
    _name="showtime.tickets"
    _description="ShowTime Tickets Description"

    name = fields.Char(required=True)
    price = fields.Integer(required=True)
    max_qty = fields.Integer()
    current_qty = fields.Integer(default=0)