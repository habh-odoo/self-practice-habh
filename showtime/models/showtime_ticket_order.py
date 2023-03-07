from odoo import fields,models,api,_,exceptions

class ShowtimeTicketOrder(models.Model):
    _name="showtime.ticket.order"
    _description="ShowTime Ticket Order Description"

    name = fields.Char(required=True,readonly=True,string="Order Reference",default = lambda self:('New'))
    ticket_id = fields.Many2one("showtime.tickets")
    buyer_id = fields.Many2one("res.partner",default= lambda self : self.env.user.partner_id)
    qty = fields.Integer(string="Quantity")
    ticket_price = fields.Integer(compute="_compute_ticket_price",string="Order Amount")
    state = fields.Selection(selection=[("new","New"),("confirm","Confirmed"),("cancel","Cancelled")],default="new")

    @api.depends("qty","ticket_id")
    def _compute_ticket_price(self):
        for record in self:
            record.ticket_price = record.ticket_id.price*record.qty

    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            vals['name'] = self.env['ir.sequence'].next_by_code('showtime.ticket.order')
        return super(ShowtimeTicketOrder,self).create(vals_list)
    
    def action_confirm_ticket(self):
        for record in self:
            if(record.state=="new"):
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
