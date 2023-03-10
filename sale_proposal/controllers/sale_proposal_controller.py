from odoo import http

class SaleProposalController(http.Controller):
    @http.route('/proposal/<model("proposal.proposal"):proposal>', auth='public', website=True)
    def index(self, proposal):
        return http.request.render('sale_proposal.proposal_details_view',{
                'proposal': proposal
            }) 