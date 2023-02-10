# -*- coding: utf-8 -*-
from odoo import fields,models

class ShowtimeSections(models.Model):
    _name="showtime.sections"
    _description="ShowTime Section Description"

    name = fields.Char(required=True)
    size = fields.Integer()
    ticket_type = fields.Many2one("showtime.tickets",string="Ticket Type")