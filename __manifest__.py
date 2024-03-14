{
    'name': "Chasqui Integration",
    'version': '1.0',
    'summary': "Integrates Odoo with the Chasqui online sales platform",
    'description': """This module extends Odoo to integrate with the Chasqui online sales platform, allowing for synchronization of products and partners between Odoo and Chasqui.""",
    'author': "Chasqui Team Developers",
    'website': "https://tiendaschasqui.ar/",
    'category': 'Sales',
    'license': 'AGPL-3',
    'depends': ['base', 'product', 'sale'],
    'data': [
        'views/product_template_views.xml',
        'views/res_partner_views.xml',
        # Puedes incluir aquí otros archivos XML o CSV que necesites para la configuración inicial, seguridad, etc.
    ],
    'demo': [
        # 'demo/demo_data.xml', # Archivos de demostración si los necesitas
    ],
    'images': ['static/description/icon-128x128.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
