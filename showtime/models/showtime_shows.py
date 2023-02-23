# -*- coding: utf-8 -*-
from odoo import fields,models,api
from dateutil.relativedelta import relativedelta

RATING = [
    ('0','No Rating'),
    ('1', 'Terrible'),
    ('2', 'Bad'),
    ('3', 'Average'),
    ('4', 'Good'),
    ('5','Great')
]

class ShowtimeShows(models.Model):
    _name="showtime.shows"
    _description="ShowTime Shows Description"

    name = fields.Char(required=True)
    description = fields.Text()
    section_id = fields.Many2one("showtime.sections",ondelete="cascade")
    venue_id = fields.Many2one("showtime.venue",related="section_id.venue_id",store=True)
    venue_type_id = fields.Many2one("showtime.venue.types",related="section_id.venue_type_id",store=True)
    start_time = fields.Datetime(required=True)
    end_time = fields.Datetime(required=True)
    ticket_ids = fields.One2many("showtime.tickets","show_id",string="Tickets",required=True)
    show_type = fields.Selection(string="Type of Seating",selection=[("open","Open Seating"),("alloted","Alloted Seating")],default="alloted",required=True)
    rating = fields.Selection(RATING,string="Rating",default="0")
    int_rating = fields.Integer(compute="_compute_int_rating",store=True)
    state = fields.Selection(selection=[("booking","Booking"),("inprogress","In-Progress"),("finished","Finished")],default="booking",compute="_compute_state",store=True)

    @api.depends("rating")
    def _compute_int_rating(self):
        for record in self:
            record.int_rating = int(record.rating)

    @api.depends("start_time","end_time")
    def _compute_state(self):
        for record in self:
            if(fields.Datetime.now()<record.start_time):
                record.state="booking"
            elif(fields.Datetime.now()>record.end_time):
                record.state="finished"
            else:
                record.state="inprogress"