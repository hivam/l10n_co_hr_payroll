# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Nómina Colombia',
    'version' : '1.0',
    'summary': 'Liquidación de nómina - Colombia',
    'description': """
This module allows
=================================================================
Modifica la liquidación de nómina en Odoo para adaptarla a la
legislación vigente en Colombia.
""",
    'category' : 'Human Resources',
    'author' : 'Hector Ivan Valencia Muñoz',
    'website': 'http://www.odoo-co.blogspot.com',
    'license': 'AGPL-3',
    'depends' : ['hr_payroll', 'hr_payroll_account'],
    'data' : [
                'views/hr_payroll_view.xml',
                'views/hr_payroll_account_view.xml',
              ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
