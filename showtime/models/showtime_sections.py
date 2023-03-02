# -*- coding: utf-8 -*-
from odoo import fields,models

class ShowtimeSections(models.Model):
    _name="showtime.sections"
    _description="ShowTime Section Description"
    _sql_constraints = [
        ("size","CHECK(size>0)","Size must be strictly Positive.")
    ]

    name = fields.Char(required=True)
    size = fields.Integer(required=True,string="Size of Section (in meters)")
    show_ids = fields.One2many("showtime.shows","section_id",string="Shows")
    venue_id = fields.Many2one("showtime.venue",ondelete="cascade")
    venue_type_id = fields.Many2one("showtime.venue.types",related="venue_id.venue_type_id")

    def name_get(self):
        result = []
        for section in self:
            name = section.venue_id.name + ' - ' + section.name
            result.append((section.id, name))
        return result

    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain=['|',('name',operator,name),('venue_id',operator,name)]
        return self._search(domain+args,limit=limit,access_rights_uid=name_get_uid)
