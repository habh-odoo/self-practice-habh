# -*- coding: utf-8 -*-
from odoo import fields,models,api
from dateutil.relativedelta import relativedelta

class ShowtimeShows(models.Model):
    _name="showtime.shows"
    _description="ShowTime Shows Description"

    name = fields.Char(required=True)
    description = fields.Text()
    section_id = fields.Many2one("showtime.sections",ondelete="cascade")
    venue_id = fields.Many2one("showtime.venue",compute="_compute_venue",store=True)
    venue_type_id = fields.Many2one("showtime.venue.types",compute="_compute_venue",store=True)
    start_time = fields.Datetime()
    end_time = fields.Datetime()
    ticket_ids = fields.One2many("showtime.tickets","show_id",string="Tickets")
    show_type = fields.Selection(string="Type of Seating",selection=[("open","Open Seating"),("alloted","Alloted Seating")],default="alloted")
        
    @api.depends("section_id")
    def _compute_venue(self):
        for record in self:
            if(record.section_id):
                record.venue_id = record.section_id.venue_id
                record.venue_type_id = record.venue_id.type_id
        