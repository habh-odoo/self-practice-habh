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
    show_id = fields.Many2one("showtime.shows")
    rows = fields.Integer(compute="_compute_max_qty",inverse="_inverse_max_qty",store=True)
    columns = fields.Integer(compute="_compute_max_qty",inverse="_inverse_max_qty",store=True)
    show_type = fields.Selection(string="Type of Seating",selection=[("open","Open Seating"),("alloted","Alloted Seating")],compute="_compute_show_type")

    @api.depends("show_id")
    def _compute_show_type(self):
        for record in self:
            record.show_type = record.show_id.show_type

    @api.depends("show_id.show_type","rows","columns")
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