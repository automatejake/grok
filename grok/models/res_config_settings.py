from odoo import fields,models

class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']
    
    grok_api_key = fields.Char(related='company_id.grok_api_key',
                               readonly=False,
                               )
    grok_version = fields.Selection([('grok-3','Grok 3'),('grok-4','Grok-4')], 
                                    related='company_id.grok_version',
                                    readonly=False)
    

class ResCompany(models.Model):
    _inherit = "res.company"

    grok_api_key = fields.Char()
    grok_version = fields.Selection([('grok-3','Grok 3'),('grok-4','Grok-4')])