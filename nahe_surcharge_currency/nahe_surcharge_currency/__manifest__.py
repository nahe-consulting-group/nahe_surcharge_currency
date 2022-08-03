# -*- coding: utf-8 -*-
{
    'name': "Moneda de Recargo en tarifas",

    'summary': """
    Moneda de Recargo en tarifas
        """,


    'description': """
        Se perimite elegir la moneda del recargo en los elementos de las tarifas, dependiendo de la necesidad de cada cliente.
        Por ejemplo se puede elegir en una tarifa en pesos que se genere un recargo en dolares al tipo de cambio configurado en Monedas
    """,

    'author': "Nähe Consulting Group",
    'website': "http://www.nahe.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
