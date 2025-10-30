from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

# Testing!!!!!

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Registration form page
@app.route('/register')
def register():
    return render_template('register.html')

# Handle form submission (students will add JSON save code here)
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    country = request.form['country']
    age = request.form['age']

    # TODO: Save form data to a JSON file (worksheet Part 1)

    flash('Registration submitted successfully!')
    return redirect(url_for('index'))

# Display stored registrations (students will add JSON reading code here)
@app.route('/view')
def view_registrations():
    # TODO: Read data from registrations.json and send to template (worksheet Part 2)

    return render_template('view.html', registrations=[])

if __name__ == '__main__':
    app.run(debug=True)
