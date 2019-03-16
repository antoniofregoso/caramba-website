# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models, tools
import logging
_logger = logging.getLogger(__name__)

class Website(models.Model):
    _inherit = "website" 
    
    floating_whatsapp_id = fields.Many2one('website.floating_whatsapp', string="Floating Whatsapp Theme")
    

    def get_whatsapp(self): 
        whatsapp = self.env['website.floating_whatsapp'].search([('id', '=', self.floating_whatsapp_id.id)])[0]
        js =  "<script type='text/javascript'>$(function () {$('#WhatsAppButton').floatingWhatsApp({phone: '" +  whatsapp.phone + "'"
        if whatsapp.message != ' ':
            js += ', message: "' + whatsapp.message + '"'
        if whatsapp.position != 'left':
            js += ', position: "' + whatsapp.position + '"'
        if whatsapp.popup_message != ' ':
            js += ', popupMessage: "' + whatsapp.popup_message + '"'
        if whatsapp.show_popup != False:
            js += ', showPopup: true'
        if whatsapp.auto_open_timeout != 0:
            js += ', autoOpenTimeout: ' + str(whatsapp.auto_open_timeout)
        if whatsapp.header_color != '#128C7E':
            js += ', headerColor: "' + whatsapp.header_color + '"'
        if whatsapp.header_title != 'WhatsApp Chat':
            js += ', headerTitle: "' + whatsapp.header_title + '"'
        if whatsapp.size != '72px':
            js += ', size: "' + whatsapp.size + '"'
        if whatsapp.background_color != '#25D366':
            js += ', backgroundColor: "' + whatsapp.background_color + '"'
        if whatsapp.button_image != ' ':
            js += ', buttonImage: \'<img src="' + whatsapp.button_image + '" />\''
        js += "});});</script>"
        return js