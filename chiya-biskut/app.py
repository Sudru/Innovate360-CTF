from flask import Flask, render_template, request, redirect, url_for, make_response
import base64

app = Flask(__name__)

# In a real application, you should use a secure method to store and check credentials.
valid_username = 'guest'
valid_password = 'guest-password'

def encode_username(username):
    return base64.b64encode(f"username={username}".encode()).decode()

def decode_username(encoded_username):
    return base64.b64decode(encoded_username.encode()).decode().split('=')[1]

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == valid_username and password == valid_password:
            encoded_username = encode_username(username)
            
            # Create a response object and set the cookie directly
            response = make_response(redirect(url_for('dashboard')))
            response.set_cookie('session', value=encoded_username)
            
            return response
        else:
            error = 'Invalid credentials. Please try again.'

    return render_template('login.html', error=error if 'error' in locals() else None)

@app.route('/dashboard')
def dashboard():
    encoded_username = request.cookies.get('session', None)

    if encoded_username:
        username = decode_username(encoded_username)
        
        # Check if the user is an admin
        is_admin = username.lower() in ['admin', 'administrator']

        return render_template('dashboard.html', username=username, is_admin=is_admin)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
