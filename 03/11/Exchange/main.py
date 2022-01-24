from datetime import datetime

import requests
import json

from khayyam import JalaliDatetime

from config import url, rulse
from notification import send_sms

from fixer import get_rates


from mailgun import send_mail



def archive(file_name, rates):
    """
    get filename and rates, save them to the speclife directory
    ;parma filename:
    ;parma rates:
    ;return: None
    """
    with open(f'archive/{file_name}.json', 'w') as f:
        f.write(json.dumps(rates))


def check_notify_rulse(rates):
    """
    Check if user defined notify rules and if rates reached to the defined
    rules, then generate proper msg to send.
    :param rates:
    :return: msg (str)
    """
    preferred = rulse['notification']['preferred']
    msg = ''
    for exc in preferred.key():
        if rates[exc] <= preferred[exc]['min']:
            msg += f'{exc} reached min: {rates[exc]} \n'
        if rates[exc] >= preferred[exc]['max']:
            msg += f'{exc} reached max: {rates[exc]} \n'
    return msg
            
        
def send_notification():
    now = JalaliDatetime(datetime.now()).strftime('%y-%B-%d  %A  %H:%M')
    msg += now
    res = send_sms(msg)


if __name__ == "__main__":
    res = get_rates(API_KEY)

    if rulse['archive']:
        archive(res['timestamp'], res['rates'])
    
    if rulse['send_mail']:
        send_mail(res['timestamp'], res['rates'])

    if rulse ['notification']['enable']:
        notification_msg = check_notify_rulse(res[rates])
        if notification_msg:
            send_notification(notification_msg)