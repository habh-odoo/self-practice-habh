# -*- coding: utf-8 -*-
from odoo import fields,models,api,exceptions
from dateutil.relativedelta import relativedelta

RATING = [
    ('0','No Rating'),
    ('1', '1 Star'),
    ('2', '2 Stars'),
    ('3', '3 Stars'),
    ('4', '4 Stars'),
    ('5','5 Stars')
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
    purchase_inprogress = fields.Boolean(default=False,string="Purchase Tickets for In-Progress Shows?")

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

    @api.constrains("start_time","end_time")
    def _constraint_time(self):
        for record in self:
            for shows in record.section_id.show_ids:
                if((record.start_time>shows.start_time and record.start_time<shows.end_time) or (record.end_time<shows.end_time and record.end_time>shows.start_time)):
                    raise exceptions.ValidationError("Shows in same Section cannot overlap.")
                elif(record.start_time==shows.start_time and record.end_time==shows.end_time and record.id!=shows.id):
                    raise exceptions.ValidationError("Shows in same Section cannot overlap.")