# -*- coding: utf-8 -*-
from odoo import fields,models

class ShowtimeVenue(models.Model):
    _name="showtime.venue"
    _description="ShowTime Venue Description"

    name=fields.Char(required=True)
    description=fields.Text()
    types = fields.Many2one("showtime.venue.types","Venue Type")
    sections = fields.Many2many("showtime.sections","Sections")