import os
import sys

from email.headerregistry import Address
from email.message import EmailMessage

import smtplib


def create_email_message(from_email_address, to_email_address, subject, body):
    """Creates a message

    Args:
        from_email_address: (obj) the address sending the email
        to_email_address: (obj) the address receiving the email
        subject: (str) the subject for the email
        body: (str) the body of the email

    Returns:
        msg: (obj) an object containing the email

    """

    msg = EmailMessage()
    msg['From'] = from_email_address
    msg['To'] = to_email_address
    msg['Subject'] = subject
    msg.set_content(body)
    return msg


# Set up sender
# Using hard coded variable
email_address = (Address(username='username', domain='gmail.com'))
email_password = 'your_password_here'

# #Using environmental variables
# email_address = os.getenv('GMAIL_ADDRESS', None)
# email_password = os.getenv('GMAIL_APPLICATION_PASSWORD', None)

# Setup recipient
to_address = (Address(username='recipient_username', domain='gmail.com'))


email_message = create_email_message(from_email_address=email_address, to_email_address=to_address, subject='Subject',
                                     body="Whatever you want to send in the body of the email",)

with smtplib.SMTP('smtp.gmail.com', port=587) as smtp_server:
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(email_address, email_password)
    smtp_server.send_message(email_message)

print('Email sent successfully')
