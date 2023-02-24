from odoo import fields,models,api,_,exceptions

class ShowtimeTicketOrder(models.Model):
    _name="showtime.ticket.order"
    _description="ShowTime Ticket Order Description"

    name = fields.Char(required=True)
    ticket_id = fields.Many2one("showtime.tickets")
    buyer = fields.Many2one("res.users")
    qty = fields.Integer(string="Quantity")
    ticket_price = fields.Integer(compute="_compute_ticket_price",string="Order Amount")
    state = fields.Selection(selection=[("new","New"),("confirm","Confirmed"),("cancel","Cancelled")],default="new")

    @api.depends("qty","ticket_id")
    def _compute_ticket_price(self):
        for record in self:
            record.ticket_price = record.ticket_id.price*record.qty

    # @api.model
    # def create(self,vals):
    #     if(vals.get('name',_('New')==_('New'))):
    #         vals['name'] = self.env['ir.sequence'].next_by_code('name') or _('New')
    #     res = super(ShowtimeTicketOrder,self).create(vals)
    #     return res
    
    def action_confirm_ticket(self):
        for record in self:
            record.ticket_id.current_qty += record.qty
            record.state="confirm"
    
    def action_cancel_ticket(self):
        for record in self:
            record.state="cancel"

    @api.constrains("qty")
    def constraint_qty(self):
        for record in self:
            if(record.qty>record.ticket_id.remaining_qty):
                raise exceptions.ValidationError("You can not purchase tickets more than the remaining quantity.")