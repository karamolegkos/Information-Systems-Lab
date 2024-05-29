from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient

# Flask App Initialization
app = Flask(__name__)
app.secret_key = 'a_random_key'  # Needed to use sessions

# MongoDB Client Initialization
client = MongoClient('localhost', 27017)  # Adjust the host and port if necessary
db = client["school_db"]  # Database name
students_collection = db["students"]
professors_collection = db["professors"]

""" Routes """
# Home Route to Home Template
@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        return render_template('home.html', username=username)
    
    # Redirect to login if not logged in
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

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        if name and surname:
            student = {'name': name, 'surname': surname}
            students_collection.insert_one(student)
            flash('Student added successfully!', 'success')
        else:
            flash('Name and Surname are required!', 'danger')
    
    return render_template('add_student.html')

@app.route('/add_professor', methods=['GET', 'POST'])
def add_professor():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        subject = request.form['subject']
        if name and surname and subject:
            professor = {'name': name, 'surname': surname, 'subject': subject}
            professors_collection.insert_one(professor)
            flash('Professor added successfully!', 'success')
        else:
            flash('Name, Surname, and Subject are required!', 'danger')
    
    return render_template('add_professor.html')

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5000)