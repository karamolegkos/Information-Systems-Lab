from flask import Flask, render_template, request, redirect, url_for, session

# Flask App Initialization
app = Flask(__name__)
app.secret_key = 'a_random_key'  # Needed to use sessions

""" Routes """
# Home Route to Home Template
@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        return render_template('home.html', username=username)
    
    # Redirect to login if not logged in (The login function)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are correct
        if username == 'admin' and password == 'admin123':
            session['username'] = username
            return redirect(url_for('home'))
        else:
            error = 'Invalid Credentials'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    # Remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5000)