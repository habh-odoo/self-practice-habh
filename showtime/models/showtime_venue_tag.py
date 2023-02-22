# -*- coding: utf-8 -*-
from odoo import fields, models

class ShowtimeVenueTag(models.Model):
    _name="showtime.venue.tag"
    _description = "Showtime Venue Tag Model _description"
    _sql_constraints = [
        ('unique_name','UNIQUE(name)','Tag Name must be unique')
    ]
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer()