# -*- coding: utf-8 -*-
from odoo import fields,models

class ShowtimeVenue(models.Model):
    _name="showtime.venue"
    _description="ShowTime Venue Description"

    name=fields.Char(required=True)
    description=fields.Text()
    owner_id = fields.Many2one("res.users",string="Owned by")
    type_id = fields.Many2one("showtime.venue.types","Venue Type")
    section_ids = fields.One2many("showtime.sections","venue_id",string="Sections")
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country')