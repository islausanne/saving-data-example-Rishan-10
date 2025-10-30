from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

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
    date_of_birth = request.form['date_of_birth']
    email = request.form['email']

    # TODO: Save form data to a JSON file (worksheet Part 1)

    flash('Registration submitted successfully!')

    # Check if file exists
    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            data = json.load(file)
    else:
        data = []

    # Add the new registration
    data.append({'name': name, 'country': country, 'date_of_birth': date_of_birth, 'email': email})

    # Save all registrations back to the file
    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    return redirect(url_for('index'))

# Display stored registrations (students will add JSON reading code here)
@app.route('/view')
def view_registrations():
    # TODO: Read data from registrations.json and send to template (worksheet Part 2)
    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            data = json.load(file)
    else:
        data = []
    return render_template('view.html', registrations=data)

@app.route('/delete')
def delete_registration():
    if os.path.exists('registrations.json'):
        os.remove('registrations.json')
        data=[]

    flash('Registrations deleted successfully!')
    return render_template('view.html', registrations=data)

if __name__ == '__main__':
    app.run(debug=True)
