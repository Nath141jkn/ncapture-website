from flask import Flask, request, render_template
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form["email"]
    license_key = request.form["license"]

    # Email setup
    sender = "ncapture13@gmail.com"
    app_password = "YOUR-APP-PASSWORD"

    msg = EmailMessage()
    msg["Subject"] = "Your NCAPTURE License Key"
    msg["From"] = sender
    msg["To"] = email
    msg.set_content(f"""
Dear NCAPTURE User,

🎉 Your license key is confirmed: {license_key}

Thanks for verifying. Stay tuned for updates!

– NCAPTURE Team
""")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(sender, app_password)
            smtp.send_message(msg)
        return "✅ License Email Sent!"
    except Exception as e:
        return f"❌ Failed to send email: {e}"

if __name__ == '__main__':
    app.run(debug=True)
