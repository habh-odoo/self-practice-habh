# -*- coding: utf-8 -*-
from odoo import fields,models

class ShowtimeSections(models.Model):
    _name="showtime.sections"
    _description="ShowTime Section Description"

    name = fields.Char(required=True)
    size = fields.Integer()
    show_ids = fields.One2many("showtime.shows","section_id",string="Shows")
    venue_id = fields.Many2one("showtime.venue")


    def show_views(self):
        return {
            'view_mode': 'gantt',
            'view_id': self.env.ref("showtime.showtime_shows_gantt").id,
            'res_model':"showtime.shows",
            'type':"ir.actions.act_window"
        }