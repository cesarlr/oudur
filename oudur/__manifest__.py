# -*- coding: utf-8 -*-
{
    'name': "oudur",

    'summary': """
        Application to control boiled eggs and see what are ready to eat
    """,

    'description': """
        Register of data associated to stored eggs. Classification of cooking.
        Size and serial number
    """,

    'author': "César López Ramírez",
    'website': "http://www.coopdevs.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ]
}
