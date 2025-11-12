{
    'name': 'Real Estate invoicing',
    'version': '18.0.1.0.0',
    'summary': 'connection real estate with invoicing',
    'author': 'Gerardo Alí Ferraro Schelijasch',
    'license': 'LGPL-3',
    'category': 'Other',
    'depends': [
        'real_estate',
        'account',
    ],
    'data': [
        'views/account_move_views.xml',
    ],
    'installable': True,
    'images': ['static/description/icon.png'],
}