# -*- coding: utf-8 -*-
from odoo import fields,models,api

class ShowtimeVenue(models.Model):
    _name="showtime.venue"
    _description="ShowTime Venue Description"

    name=fields.Char(required=True)
    description=fields.Text()
    owner_id = fields.Many2one("res.partner",string="Owned by",required=True)
    venue_type_id = fields.Many2one("showtime.venue.types","Venue Type")
    tag_ids = fields.Many2many("showtime.venue.tag")
    section_ids = fields.One2many("showtime.sections","venue_id",string="Sections")
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country')
    section_count = fields.Integer(compute="_compute_section_count",default=0)
    show_count = fields.Integer(compute="_compute_show_count",default = 0)

    @api.depends("section_ids")
    def _compute_show_count(self):
        for record in self:
            if(record.section_ids):
                if(record.section_ids.mapped("show_ids")):
                    record.show_count = len(record.section_ids.mapped("show_ids"))
                else:
                    record.show_count = 0
            else:
                record.show_count = 0

    @api.depends("section_ids")
    def _compute_section_count(self):
        for record in self:
            record.section_count = len(record.mapped("section_ids"))

    def action_view_shows(self):
        action = self.env["ir.actions.actions"]._for_xml_id("showtime.showtime_shows_action")
        action.update({
            'domain': [('venue_id', '=', self.id)],
        })
        return action
