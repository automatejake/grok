from odoo import http
import requests
import json

class SpreadsheetController(http.Controller):
    @http.route('/spreadsheet/grok', type='json', auth='user')
    def grok_api(self, **kw):
        try:
            api_url = "https://api.x.ai/v1/chat/completions"
            api_key = http.request.env.company.grok_api_key
            
            if not api_key:
                return {'error': 'You need to set your API key in settings'}

            response = http.request.get_json_data()
            prompt = response['prompt']

            response = requests.post(
                api_url,
                headers={
                    'Authorization': f'Bearer {api_key}',
                    'Content-Type': 'application/json'
                },
                json={
                "messages": [{
                    "role": "system",
                    "content": "You are an assistant designed to extract, clean, or find data without any explanation of how you came to a response."
                },{
                    "role": "user",
                    "content": prompt
                }]
            }
            )
            data = response.json()
            if('error') in data:
                return {'error': data['error']}
            
            result = data['choices'][0]['message']['content']
            return result
        except Exception as e:
            return {'error': str(e)}