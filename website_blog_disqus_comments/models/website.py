# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models, tools

class Website(models.Model):
    _inherit = "website" 
    
    disqus_website = fields.Char('Disqus Subdomain', help='XXXX.disqus.com', default='XXXX')
    
    
    def get_disqus(self, blog_post_url, blog_post_id):
        disqus_script = '''<script>
        /*
        var disqus_config = function () {
        this.page.url = %s; 
        this.page.identifier = %s;
        };
        */
        (function() { 
        var d = document, s = d.createElement('script');
        s.src = 'https://%s.disqus.com/embed.js';
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
        })();
        </script>
        <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>''' % (blog_post_url,blog_post_id, self.disqus_website)
        return disqus_script
        