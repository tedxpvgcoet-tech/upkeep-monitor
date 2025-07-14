from mail_utils import send_email
import json
import os

password = os.environ.get("EMAIL_PASSWORD")
attachment_paths = []

total_time = 0
count = 0

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), '..', 'data', 'internal_team.json')
)

with open(filepath, 'r') as list:
  recipients = json.load(list)

for recipient in recipients:
  try:
    subject = "🚨 Backend Alert"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>{subject}</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #fff3f3; padding: 20px;">
      <div style="max-width: 600px; margin: auto; background-color: #ffffff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); padding: 20px; border-left: 6px solid #d11a2a;">
        <h2 style="color: #d11a2a;">🚨 Backend Is Currently Offline</h2>
        
        <p>Hi {recipient['name']},</p>

        <p>We attempted to ping the backend at:</p>

        <p style="color: #d11a2a;"><strong>Status:</strong> ❌ Offline or unresponsive</p>

        <p>This alert is sent because the backend did not respond as expected during our scheduled uptime check. Please investigate if the service is down or in sleep mode.</p>

        <hr style="border: none; border-top: 1px solid #eee; margin: 24px 0;" />

        <p style="font-size: 0.9em; color: #555;">This is an automated alert from the TEDxPVGCOET uptime monitor. Please contact Jagdish or Tanushka from the Tech Team if you're seeing this!</p>

        <p>Regards,<br/><strong>TEDxPVGCOET Automation-Mailing Bot 🤖</strong></p>
      </div>
    </body>
    </html>
    """
    print(f"Sending mail to {recipient['name']} ({recipient['email']})...")
    this_time = send_email(recipient["email"], subject, body, password, attachment_paths)
    if this_time > 0:
      count += 1
      total_time += this_time
  except Exception as e:
    print(f"Failed to send mail to {recipient}: {e}")
