import smtplib
import requests
import json

from config import EMAIL_RECIVER
from local_config import MAILGUN_APIKEY

from khayyam import JalaliDatetime
from email.mime.text import MIMEText

from datetime import datetime

# Api
def send_api_email(subject, body):
    return requests.post(
        "https://api.mailgun.net/v3/inprobes/messages",
        auth=("api", MAILGUN_APIKEY),
        data={
            "from": "Simple email.com",
            "to": ["Simple email-2.com", "Simple email-3.com"],
            "subject": subject,
            "text": body
        }
    )


def send_smtp_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "finance@inprobes.com"
    msg['To'] = rulse['email']['receiver']

    with smtplib.SMTP('smtp.mailgun.org', 587) as mail_server:
        mail_server.login('postmaster@mg.inprobes.com', MAILGUN_APIKEY)
        mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
        # mail_server.quit()


def send_mail(timestamp, rates):
    """
    get timestamp and rates, check if there is preferre
    then send email through smtp
    :param timestamp:
    :param rates:
    """
    now = JalaliDatetime(datetime.now()).strftime('%y-%B-%d  %A  %H:%M')
    subject = f'{timestamp} - {datetime.now()} rates'
    if rulse['email']['preferred'] is not None:
        tmp = dic()
        for exc in rulse['preferred']:
            tmp[exc] = rates[exc]
        rates = tmp

    text = json.dumps(rates)

    send_smtp_email(subject, text)
