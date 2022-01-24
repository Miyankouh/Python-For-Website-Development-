# BASE_PATH = 'http://data.fixer.io/api/latest?access_key='
API_KEY = 'ab7780455b7435413eb6d274c45724b5'
# url = BASE_PATH + API_KEY


EMAIL_RECIVER = 'simple email address'

# 
# rulse = {
    # 'archive': True,
    # 'send_mail': True,
    # # preferred default is None
    # #'preferred': None,
    # 'preferred': ['BTC','IRR','USD','CAD','AUD','GBP','NZD','JPY','CHF'],
    # 'notification': True,
# }

rulse = {
    'archive': True,
    'email':{
        'receiver': 'simple@',
        'preferred': ['BTC','IRR','USD','CAD','AUD','GBP','NZD','JPY','CHF'],
    },
    'notification': {
        'enabled': True,
        'receiver': 'simple number',
        'preferred':{
            'BTC': {'min': 2.9024428e-05, 'max': 2.9824428e-05},
            'USD': {'min': 1.134044, 'max': 1.154044},
            }
    }

}