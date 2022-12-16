from flask import Flask, render_template, request, redirect, url_for, session
from google.oauth2.credentials import Credentials
import google.auth.transport.requests
import requests

app = Flask(__name__)

@app.route('/')
def index():
    if 'credentials' not in session:
        return render_template('login.html')
    return 'You are already logged in'

@app.route('/login')
def login():
    # Generate the Google Sign-In URL
    google_auth = google.oauth2.credentials.Credentials.from_authorized_user_info(info=request.form)
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
