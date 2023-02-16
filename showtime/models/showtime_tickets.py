# -*- coding: utf-8 -*-
from odoo import fields,models,api

class ShowtimeTickets(models.Model):
    _name="showtime.tickets"
    _description="ShowTime Tickets Description"
    _sql_constraints = [
        ("price","CHECK(price>=0)","The Price should be Positive.")
    ]

    name = fields.Char(required=True)
    price = fields.Integer(required=True)
    max_qty = fields.Integer(string="Total Tickets")
    current_qty = fields.Integer(required=True,default=0,string="Booked Tickets")
    show_id = fields.Many2one("showtime.shows")