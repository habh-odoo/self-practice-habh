# -*- coding: utf-8 -*-
from odoo import models,Command

class ShowtimeTicketOrder(models.Model):
    _inherit = "showtime.ticket.order"

    def action_confirm_ticket(self):
        vals = {'partner_id':self.buyer_id.id,'move_type':'out_invoice','invoice_line_ids':[
            Command.create({
                "name": self.ticket_id.name,
                "quantity":self.qty,
                "price_unit":self.ticket_id.price
            })
        ]}
        self.env["account.move"].create(vals)
        return super(ShowtimeTicketOrder,self).action_confirm_ticket()