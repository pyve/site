# -*- coding: utf-8 -*-
{
    'name': "PyVe Site",

    'summary': """
        Pyve init module
    """,

    'author': "Python Venezuela,"
              "Vauxoo",  # Just testing the linter

    # Everybody can read this code,
    # no matter why or where
    # This should be always publically available.
    # That's Why agpl is the best option.
    'license': 'AGPL-3',

    'contributors': [
        "Nhomar Hernandez <nhomar@gmail.com>",
    ],

    'website': "http://www.python.org.ve",

    # Categories can be used to filter modules in modules listing
    # Check on odoo openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Specific Industry Applications',

    # Following OCA's versioning strategy.
    'version': '9.0.0.0.1',

    # any module necessary for this one to work correctly
    # try to add only the lower levels.
    # For example: if you need account_accountant do not
    # add account because one depends of the another.
    'depends': [
        'website_blog',
        'website_event',
        'website_forum_doc',
        'website_twitter',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',  # custom global layout.
        'data/configuration.yml',  # Configuration automatic.
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
