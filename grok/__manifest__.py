{
    'name': 'Grok Spreadsheet Function',
    'version': '1.0',
    'category': 'Productivity',
    'depends': ['spreadsheet'],
    'license': 'OPL-1',
    'price': 0,
    'currency': 'USD',
    'author': "BizyLife",
    'website': "https://www.bizylife.com/r/GrokSpreadsheets",
    'images': ["static/description/images/banner.gif"],
    'data': [
        'views/res_config_settings.xml',
    ],
    'assets': {
        'spreadsheet.o_spreadsheet': [
            (
                'after',
                'spreadsheet/static/src/o_spreadsheet/o_spreadsheet.js',
                'grok_spreadsheets/static/src/**/*.js'
            ),
        ],
    },
    'installable': True,
    'auto_install': False,
}