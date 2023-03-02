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
    max_qty = fields.Integer(string="Total Tickets",compute="_compute_max_qty",store=True,inverse="_inverse_max_qty",default=0)
    current_qty = fields.Integer(required=True,default=0,string="Booked Tickets")
    remaining_qty = fields.Integer(compute="_compute_remaining_qty")
    show_id = fields.Many2one("showtime.shows")
    rows = fields.Integer(compute="_compute_max_qty",inverse="_inverse_max_qty",store=True)
    columns = fields.Integer(compute="_compute_max_qty",inverse="_inverse_max_qty",store=True)
    show_type = fields.Selection(string="Type of Seating",related="show_id.show_type")
    order_ids = fields.One2many("showtime.ticket.order","ticket_id")

    @api.depends("current_qty","max_qty")
    def _compute_remaining_qty(self):
        for record in self:
            record.remaining_qty = record.max_qty-record.current_qty
    
    @api.depends("show_type","rows","columns")
    def _compute_max_qty(self):
        for record in self:
            if(record.show_type=="alloted"):
                if(record.rows and record.columns):
                    record.max_qty = record.rows*record.columns
            else:
                record.rows=""
                record.columns=""
    
    def _inverse_max_qty(self):
        for record in self:
            if(record.show_type=="alloted"):
                if(record.rows and record.columns):
                    record.max_qty = record.rows*record.columns
