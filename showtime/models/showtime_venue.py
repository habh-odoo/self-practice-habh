# -*- coding: utf-8 -*-
from odoo import fields,models

class ShowtimeVenue(models.Model):
    _name="showtime.venue"
    _description="ShowTime Venue Description"

    name=fields.Char(required=True)
    description=fields.Text()
    type=fields.Selection(string="Venue Type",selection=[("theatre","Theatre"),("party_plot","Party Plot"),("stage","Stage")])