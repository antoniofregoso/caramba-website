# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
{
    'name': "Website Floating Whatsapp",

    'summary': "Floating button for WhatsApp",

    'description': """
        This is a very simple floating WhatsApp button plugin for jQuery.

        It adds a floating-like button to your site that calls the WhatsApp Click to Chat API.

        It will automatically begin a WhatsApp chat with the number set when the user clicks the button.

        You an also activate a fake chat window with a customized message where the user can input their reply before opening WhatsApp.
    """,

    'author': "Antonio Fregoso",
    'website': "http://www.antoniofregoso.blog",
    'category': 'website',
    'version': '12.0.0.0.0',

    'depends': ['website','web_widget_color'],

    
     'data': [
        'security/ir.model.access.csv',
        'views/website_floating_whatsapp_views.xml',
        'views/res_config_view.xml',
        'views/templates.xml',
        'data/website_floating_whatsapp_data.xml'
    ],
  
}