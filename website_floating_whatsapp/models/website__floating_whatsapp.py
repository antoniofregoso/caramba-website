# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models, tools

class Website(models.Model):
    _name = 'website.floating_whatsapp'
    _description = 'Floating Whatsapp'
    
    name = fields.Char()
    phone = fields.Char('Name', help='WhatsApp intenational number which will receive the message.', required=True)
    message = fields.Char('Message', default=' ', help='Message to be sent. If showPopup is true, the input will be populated with this message.')
    position = fields.Selection([('left', 'Left'), ('right', 'Right')], default='left', String='Selection', help='Position of the button the screen.')
    popup_message = fields.Char('Popup Message', default=' ', help='Message to be shown as a received message in the fake chat.')
    show_popup = fields.Boolean('Show Popup', defaut=False, help='Show a fake chat popup when the user hovers (on desktop) or clicks the button (on mobile).')
    auto_open_timeout = fields.Integer('Auto Open Time Out', default=0, help='Set an amount of time in milliseconds for the popup to open automaticaly.')
    header_color = fields.Char('Header Color', size=7, default='#128C7E')
    header_title = fields.Char('Header Title', default='WhatsApp Chat', help='Text to be displayed at the popup window title bar.')
    size = fields.Char('Size', default='72px', help='The size of the button.')
    background_color = fields.Char('Background color', size=7, default='#25D366')
    button_image =  fields.Char('Button Image', default=' ', help='Button background image. Must be an img or svg in order to be displayed properly. <img src="burger.svg" />' )
    
    
    