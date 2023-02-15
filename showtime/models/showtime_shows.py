# -*- coding: utf-8 -*-
from odoo import fields,models,api
from dateutil.relativedelta import relativedelta

def roundtime(time):
    return time.replace(second=0,microsecond=0,minute=0,hour=time.hour+1)

class ShowtimeShows(models.Model):
    _name="showtime.shows"
    _description="ShowTime Shows Description"

    name = fields.Char(required=True)
    section_id = fields.Many2one("showtime.sections",ondelete="cascade")
    venue_id = fields.Many2one("showtime.venue")
    venue_type_id = fields.Many2one("showtime.venue.types")
    start_time = fields.Datetime(default=lambda self: roundtime(fields.Datetime.now()))
    end_time = fields.Datetime(default=lambda self: roundtime(fields.Datetime.now())+relativedelta(hours=2))
    ticket_ids = fields.One2many("showtime.tickets","show_id",string="Tickets")
    show_type = fields.Selection(string="Type of Seating",selection=[("open","Open Seating"),("alloted","Alloted Seating")],default="alloted")
        
    @api.onchange("section_id")
    def _onchange_section_id(self):
        self.venue_id = self.section_id.venue_id
        self.venue_type_id = self.venue_id.type_id
        