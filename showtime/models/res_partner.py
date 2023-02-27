# -*- coding: utf-8 -*-
from odoo import fields,models

class ResPartner(models.Model):
    _name="res.partner"
    _inherit="res.partner"

    venue_ids = fields.One2many("showtime.venue","owner_id")