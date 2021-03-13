import smtplib
from email.message import EmailMessage
from string import Template

# You don't have to put [] on the script
email = EmailMessage()
email["from"] = "[Your Name]"
email["to"] = "[Email to recive]"
email["subject"] = "[The subject of the mail]"

email.set_content("[The message of the mail]")

with smtplib.SMTP(host="[SMTP server name]", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("[Your email]",
               "[Your passwor or the app password if you use gmail]")
    smtp.send_message(email)
    print("[If you want to print any message in the console after sending the mail]")
