from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# CONFIGURE THESE
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
RECEIVER_EMAIL = "info@shaluxedesigns.co.ke"


@app.route("/")
def index():
    return render_template("index.html")  # your HTML file


@app.route("/subscribe", methods=["POST"])
def subscribe():
    user_email = request.form.get("email")

    if not user_email:
        return "Email is required", 400

    subject = "New Subscription"
    body = f"New user subscribed with email: {user_email}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECEIVER_EMAIL

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        return "Subscription successful!"
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
