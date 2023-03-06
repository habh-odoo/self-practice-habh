# -*- coding: utf-8 -*-
{
    'name':"Sale Proposal",
    'depends':['base','sale_management'],
    'license':"LGPL-3",
    'installable': True,
    'auto_install': True,
    'data':[
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/sale_proposal_views.xml',
        'views/sale_menus.xml',
        ],
}
