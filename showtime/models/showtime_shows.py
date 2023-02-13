# -*- coding: utf-8 -*-
from odoo import fields,models

class ShowtimeShows(models.Model):
    _name="showtime.shows"
    _description="ShowTime Shows Description"

    name = fields.Char(required=True)
    section_id = fields.Many2one("showtime.sections")
    start_time = fields.Datetime()
    end_time = fields.Datetime()
    ticket_ids = fields.One2many("showtime.tickets","show_id",string="Tickets")
    