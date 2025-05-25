from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/send', methods=['GET'])
def send_email():
    recipient = request.args.get('to', 'ncapture13@gmail.com')
    key = request.args.get('key', 'No license key provided')

    msg = MIMEText(f"Hello, your NCAPTURE license key is:\n\n{key}")
    msg['Subject'] = "Your NCAPTURE License Key"
    msg['From'] = "ncapture13@gmail.com"
    msg['To'] = recipient

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("ncapture13@gmail.com", "bwfdhjxkhizizltz")
    server.sendmail("ncapture13@gmail.com", recipient, msg.as_string())
    server.quit()

    return "Email sent successfully!"

if __name__ == '__main__':
    app.run(debug=True)
