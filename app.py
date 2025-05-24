from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'NCAPTURE License Server is Running'

@app.route('/send', methods=['GET'])
def send_email():
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"

    # Get parameters from the URL
    recipient_email = request.args.get('to')
    license_key = request.args.get('key')

    # Validate inputs
    if not recipient_email or not license_key:
        return jsonify({'error': 'Missing "to" or "key" parameter'}), 400

    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = 'Your NCAPTURE License Key'
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content(f"Hello,\n\nYour NCAPTURE 13 license key is:\n\n{license_key}\n\nThank you for your purchase!")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        return jsonify({'status': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
