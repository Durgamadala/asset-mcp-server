from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

# Load environment variables
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Create MCP Server
mcp = FastMCP("Asset Operations Server")


@mcp.tool()
def approve_request(
    request_id: str,
    asset_name: str,
    department: str
) -> dict:
    """
    Approves asset requests based on predefined rules.
    """

    auto_approved_assets = [
        "Laptop",
        "Monitor",
        "Keyboard",
        "Mouse"
    ]

    if asset_name.strip().title() in auto_approved_assets:
        return {
            "request_id": request_id,
            "asset_name": asset_name,
            "department": department,
            "approval_status": "Approved"
        }

    return {
        "request_id": request_id,
        "asset_name": asset_name,
        "department": department,
        "approval_status": "Pending Manual Approval"
    }


@mcp.tool()
def send_email(
    employee_name: str,
    email: str,
    asset_name: str,
    request_id: str,
    approval_status: str
) -> dict:
    """
    Sends asset request status email.
    """

    subject = "Asset Request Update"

    body = f"""
Hello {employee_name},

Your asset request has been processed.

Request ID: {request_id}
Asset: {asset_name}
Status: {approval_status}

Regards,
IT Asset Team
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        return {
            "status": "Success",
            "message": f"Email sent to {email}"
        }

    except Exception as e:
        return {
            "status": "Failed",
            "message": str(e)
        }


print("Registered tools:")
print("- approve_request")
print("- send_email")

if __name__ == "__main__":
    print("Starting Asset MCP Server...")
    mcp.run()