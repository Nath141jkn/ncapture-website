from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    with open("index.html") as f:
        return render_template_string(f.read())

@app.route('/verify', methods=['POST'])
def verify():
    name = request.form['name'].strip()
    email = request.form['email'].strip()
    license_key = request.form['license'].strip()

    found = False
    with open("sent_licenses.txt", "r") as file:
        for line in file:
            if name in line and email in line and license_key in line:
                found = True
                break

    if found:
        return "<h2 style='color:green;'>License is VALID!</h2>"
    else:
        return "<h2 style='color:red;'>License NOT found!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
