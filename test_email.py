from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

recipient_email = input("Enter recipient email: ")

subject = "MCP Email Test"

body = """
Hello,

This is a test email from the Asset MCP Server.

Regards,
Asset Operations Team
"""

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = EMAIL_ADDRESS
msg["To"] = recipient_email

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

    print(f"Email sent successfully to {recipient_email}")

except Exception as e:
    print("Error:", e)