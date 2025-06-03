import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send_email(
        subject: str="Daily Financial Ideas", 
        body: str="Here are your daily financial ideas!",
        receiver_email: str="iitbhu.bhupendra@gmail.com"
    ) -> bool:
    sender_email=os.getenv("SENDER_EMAIL")
    app_password=os.getenv("APP_PASSWORD")

    try:
        # Create email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to Gmail SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        print("✅ Email sent successfully!")
        return True

    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

send_email()