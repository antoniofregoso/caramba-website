# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import models, fields, api, _

OWL_DEFAULT = {'items':3, 'Loop':False, 'center':'False', 'Rewind':'False', 'Check Visibility':True,
               ' mouseDrag':True, 'touchDrag':True, 'pullDrag':True, 'freeDrag':False, 
               'margin':0, 'stagePadding':0, 
                'merge':False, 'mergeFit':True, 'autoWidth':False, 
                'startPosition':0, 'rtl':False,
                'smartSpeed':250, 'fluidSpeed':False, 'dragEndSpeed':False, 
                'responsive':'{}', 'responsiveRefreshRate':200, 'responsiveBaseElement':'window',
                'fallbackEasing':True, 'slideTransition':True, 
                'info':False,
                'nestedItemSelector':False, 'itemElement':"'div'", 'stageElement':"'div'",
                'refreshClass':"'owl-refresh'", 'loadedClass':"'owl-loaded'", 'loadingClass':"'owl-loaded'",
                'rtlClass':"'owl-rtl'", 'responsiveClass':"'owl-responsive'", 'dragClass':"'owl-drag'",
                'itemClass':"'owl-item'", 'stageClass':"'owl-stage'", 'stageOuterClass':"'owl-stage-outer'", 
                'grabClass':"'owl-grab'"
                    }


class Owl(models.Model):
    _name = 'website.owl'
    _description = 'Website Owl Carousel'
    
    name = fields.Char('Carousel Name', required=True)
    items = fields.integer('Items', default=3, required=True)
    loop = fields.Boolean('Loop', default=False, required=True)
    center = fields.Boolean('Center', default=False, required=True)
    rewind = fields.Boolean('Rewind', default=False, required=True)
    checkVisibility = fields.Boolean('Check Visibility', default=True, required=True)
    
    mouseDrag = fields.Boolean('Mouse Drag', default=True, required=True)
    touchDrag = fields.Boolean('Touch Drag', default=True, required=True)
    pullDrag = fields.Boolean('Pull Drag', default=True, required=True)
    freeDrag = fields.Boolean('Free Drag', default=False, required=True)

    margin = fields.integer('Margin', default=0, required=True)
    stagePadding = fields.integer('Stage Padding', default=0, required=True)

    merge = fields.Boolean('Merge', default=False, required=True)
    mergeFit = fields.Boolean('Merge Fit', default=True), required=True
    autoWidth = fields.Boolean('Auto Drag', default=False, required=True)

    startPosition = fields.integer('Start Position', default=0, required=True)
    rtl = fields.Boolean('RTL', default=False, required=True)

    smartSpeed = fields.integer('Smart Speed', default=250, required=True)
    fluidSpeed = fields.Boolean('Fluid Speed', default=False, required=True)
    dragEndSpeed = fields.Boolean('Drag End Speed', default=False, required=True)

    responsive = fields.Char('Responsive', default ='{}', required=True)
    responsiveRefreshRate = fields.integer('Responsive Refresh Rate', default=200, required=True)
    responsiveBaseElement = fields.Char('Responsive Base Element', default ='window', required=True)

    fallbackEasing = fields.Char('Fall Back Easing', default ="'swing'", required=True)
    slideTransition = fields.Char('Slide Transition', default ="''", required=True)

    info = fields.Boolean('Info', default=False)

    nestedItemSelector = fields.Boolean('Nested Item Selector', default=False, required=True)
    itemElement = fields.Char('Item Element', default ="'div'", required=True)
    stageElement = fields.Char('Stage Element', default ="'div'", required=True)

    refreshClass = fields.Char('Refresh Class', default ="'owl-refresh'", required=True)
    loadedClass = fields.Char('Loaded Class', default ="'owl-loaded'", required=True)
    loadingClass = fields.Char('Loading Class', default ="'owl-loaded'", required=True)
    rtlClass = fields.Char('RTL Class', default ="'owl-rtl'", required=True) 
    responsiveClass = fields.Char('Responsive Class', default ="'owl-responsive'", required=True) 
    dragClass = fields.Char('Drag Class', default ="'owl-drag'", required=True) 
    itemClass = fields.Char('Item Class', default ="'owl-item'", required=True) 
    stageClass = fields.Char('Stage Class', default ="'owl-stage'", required=True) 
    stageOuterClass = fields.Char('Stage Outer Class', default ="'owl-stage-outer'", required=True)
    grabClass = fields.Char('Grab Class', default ="'owl-grab'", required=True) 
    
    
    
    
       