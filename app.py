from flask import Flask, request, render_template, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
# Required for session-based flash messages
app.secret_key = 'super_secret_key_change_this' 

# CONFIGURATION
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password" # Use a Google App Password
RECEIVER_EMAIL = "info@shaluxedesigns.co.ke"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/subscribe", methods=["POST"])
def subscribe():
    user_email = request.form.get("email")

    if not user_email:
        flash("Email is required!", "error")
        return redirect(url_for('index'))

    # Compose the email
    msg = MIMEText(f"New user subscribed with email: {user_email}")
    msg["Subject"] = "New Subscription: Shaluxe Designs"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECEIVER_EMAIL

    try:
        # Connect and send
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        
        flash("Thanks for subscribing!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "error")

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
