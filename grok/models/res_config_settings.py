from odoo import fields,models

class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']
    
    grok_api_key = fields.Char(related='company_id.grok_api_key',
                               readonly=False,
                            #    check_company=True,
                               )
    

class ResCompany(models.Model):
    _inherit = "res.company"

    grok_api_key = fields.Char()
    