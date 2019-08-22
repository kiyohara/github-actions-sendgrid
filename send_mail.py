import os

import sendgrid
from sendgrid.helpers.mail import *

import base64

api_key   = os.environ.get('SENDGRID_API_KEY')
from_addr = os.environ.get('SENDGRID_MAIL_FROM')
to_addr   = os.environ.get('SENDGRID_MAIL_TO')
git_tag   = os.environ.get('GITHUB_REF')

subject = "Sending with SendGrid is Fun (%s)" % git_tag
plain_text_content = """
and easy to do anywhere, even with Python
and easy to do anywhere, even with Python
and easy to do anywhere, even with Python
"""
"""
if CR is removed, set SendGrid 'Plain Content' setting as 'ACTIVE'
ref. Settings > Mail Settings > Plain Content
"""

message = Mail(
    from_email=from_addr,
    to_emails=[to_addr],
    subject=subject,
    plain_text_content=plain_text_content)

# attached-file.txt handling
with open("attached-file.txt", "rb") as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()

attachment = Attachment()
attachment.file_content = FileContent(encoded)
attachment.file_type = FileType('text/plain')
attachment.file_name = FileName('attached-file.txt')
attachment.disposition = Disposition('attachment')
message.attachment = attachment

try:
    sendgrid_client = sendgrid.SendGridAPIClient(api_key)
    response = sendgrid_client.send(message)

    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)

