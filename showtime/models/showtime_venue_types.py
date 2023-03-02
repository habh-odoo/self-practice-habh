# -*- coding: utf-8 -*-
from odoo import fields,models

class ShowtimeVenueTypes(models.Model):
    _name="showtime.venue.types"
    _description="ShowTime Venue Types Description"
    _sql_constraints = [
        ('unique_name','UNIQUE(name)','Tag Name must be unique')
    ]
    _order = "sequence"

    name = fields.Char(required=True)
    sequence = fields.Integer("Sequence",default=1)
