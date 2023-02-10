# -*- coding: utf-8 -*-
from odoo import fields,models

class ShowtimeVenueTypes(models.Model):
    _name="showtime.venue.types"
    _description="ShowTime Venue Types Description"

    name = fields.Char(required=True)
    