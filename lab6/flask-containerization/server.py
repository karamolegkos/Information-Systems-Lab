from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
import os

# Flask App Initialization
app = Flask(__name__)
app.secret_key = 'a_random_key'  # Needed to use sessions

SERVER_HOST = os.environ.get('SERVER_HOST', 'localhost')
SERVER_PORT = int(os.environ.get('SERVER_PORT', 5000))
MONGO_DATABASE = os.environ.get('MONGO_DATABASE', 'school_db')
MOGNO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.environ.get('MONGO_PORT', 27017))

# MongoDB Client Initialization
client = MongoClient(MOGNO_HOST, MONGO_PORT)
db = client[MONGO_DATABASE]  # Database name
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

    students = list(students_collection.find())
    return render_template('add_student.html', students=students)

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

    professors = list(professors_collection.find())
    return render_template('add_professor.html', professors=professors)

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True, host=SERVER_HOST, port=SERVER_PORT)