# -*- coding: utf-8 -*-
from odoo import fields,models,api,_
import datetime
class ProposalProposal(models.Model):
    _name = "proposal.proposal"
    _description = "Proposal Model"
    _inherit=["sale.order"]

    name = fields.Char()
    state = fields.Selection(string="Status",
        required=True,
        selection=[("draft","Draft"),("sent","Sent"),("confirm","Confirmed")],
        default="draft",
    )
    transaction_ids = fields.Many2many("payment.transaction",relation="proposal_transaction_rel")
    tag_ids = fields.Many2many("crm.tag",relation="proposal_tag_rel")
    status = fields.Selection(string="Proposal Status",
                              selection=[("notreview","Not Reviewed"),("approved","Approved"),("rejected","Rejected")],
                              default="notreview",
                              required=True)
    sale_order_id = fields.Many2one("sale.order")
    order_line = fields.One2many("sale.order.line.proposal","order_id")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'company_id' in vals:
                self = self.with_company(vals['company_id'])
            if vals.get('name', _("New")) == _("New"):
                seq_date = fields.Datetime.context_timestamp(
                    self, fields.Datetime.to_datetime(vals['date_order'])
                ) if 'date_order' in vals else None
                name = self.env['ir.sequence'].next_by_code(
                    'proposal.proposal', sequence_date=seq_date) or _("New")
                
                now = datetime.datetime.now()
                year = now.strftime("%Y")
                month = now.strftime("%b")
                name = name.replace("prefix_key","Proposal/"+year+'/'+month+'/')
                vals['name'] = name

        return super().create(vals_list)
    
    def action_quotation_send(self):
        """ Opens a wizard to compose an email, with relevant mail template loaded by default """
        self.ensure_one()
        lang = self.env.context.get('lang')
        mail_template = self._find_mail_template()
        if mail_template and mail_template.lang:
            lang = mail_template._render_lang(self.ids)[self.id]
        ctx = {
            'default_model': 'proposal.proposal',
            'default_res_id': self.id,
            'default_use_template': bool(mail_template),
            'default_template_id': mail_template.id if mail_template else None,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'default_email_layout_xmlid': 'mail.mail_notification_layout_with_responsible_signature',
            'proforma': self.env.context.get('proforma', False),
            'force_email': True,
            'model_description': self.with_context(lang=lang).type_name,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }
    
    def _find_mail_template(self):
        """ Get the appropriate mail template for the current sales order based on its state.

        If the SO is confirmed, we return the mail template for the sale confirmation.
        Otherwise, we return the quotation email template.

        :return: The correct mail template based on the current status
        :rtype: record of `mail.template` or `None` if not found
        """
        self.ensure_one()
        return self.env.ref('sale_proposal.email_template', raise_if_not_found=False)