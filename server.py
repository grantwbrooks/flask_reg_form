from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'[0-9]')
PASS_REGEX = re.compile(r'.*[A-Z].*[0-9]')

app = Flask(__name__)
app.secret_key = "ThisIsSecretadfasdfasdf!"

@app.route('/')
def index():
    print session
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def get_name():

    print request.form
    print request.form['email']
    print session

    for x in request.form:
        if len(request.form[x]) < 1:
            flash(x + " cannot be blank!", 'blank')
    
    # if not request.form['first_name'].isalpha():
    if NAME_REGEX.search(request.form['first_name']):
        flash("First name cannot contain any numbers", 'error')
    if NAME_REGEX.search(request.form['last_name']):
        flash("Last name cannot contain any numbers", 'error')

    if len(request.form['password']) < 8:
        flash("Password must be more than 8 characters", 'password')

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email must be a valid email", 'error')
    
    if not PASS_REGEX.search(request.form['password']):
        flash("Password must have a number and an uppercase letter", 'password')
    
    if request.form['password'] != request.form['confirm_password']:
        flash("Password and Password Confirmation should match", 'password')



# The line below is key so you get all of the error messages to display on the first page and then the all good message if no flashes, all good is another flash
    if '_flashes' in session:
# changed this line to be render so I could put in value = on the html page to save what the person typed when it didn't validate
        return render_template('index.html')
    else:
        flash("All Good!!!!", 'good')
        return redirect('/')
#didn't get the hacker version done with the birthday stuff

app.run(debug=True)