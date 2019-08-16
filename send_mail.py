import os

import sendgrid
from sendgrid.helpers.mail import *

import base64

api_key   = os.environ.get('SENDGRID_API_KEY')
from_addr = os.environ.get('SENDGRID_MAIL_FROM')
to_addr   = os.environ.get('SENDGRID_MAIL_TO')
git_tag   = os.environ.get('CIRCLE_TAG')

sg = sendgrid.SendGridAPIClient(apikey=api_key)
from_email = Email(from_addr)
to_email = Email(to_addr)
subject = "Sending with SendGrid is Fun (%s)" % git_tag
content = Content("text/plain", """
and easy to do anywhere, even with Python
and easy to do anywhere, even with Python
and easy to do anywhere, even with Python
""")
"""
if CR is removed, set SendGrid 'Plain Content' setting as 'ACTIVE'
ref. Settings > Mail Settings > Plain Content
"""

mail = Mail(from_email, subject, to_email, content)

# attached-file.txt handling
with open("attached-file.txt", "rb") as f:
  attached_base64 = base64.b64encode(f.read()).decode("ascii")

attachment = Attachment()
attachment.type = "text/plain"
attachment.filename = "attached-file.txt"
attachment.content = attached_base64
attachment.disposition = "attachment"
mail.add_attachment(attachment)

response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
