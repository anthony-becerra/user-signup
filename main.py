from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('user_signup_form.html')

@app.route("/", methods=['POST'])
def validate_form():
    # Set variables from POST request
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
    
    # Error if username or password has less than 3 characters or more than 20
    if len(username) < 3 or len(username) > 20:
        username_error = "That's not a valid username (must be between 3-20 characters long)"

    if len(password) < 3 or len(password) > 20:
        password_error = "That's not a valid password (must be between 3-20 characters long)"
    
    # Error if user leaves any of the following fields empty: username, password, verify password
    if username == '':
        username_error = "That's not a valid username"
    if password == '':
        password_error = "That's not a valid password"
    if verify_password == '':
        verify_password_error = "Passwords don't match"
    
    # Error if the user's password and password-confirmation do not match.
    if password != verify_password:
        verify_password_error = "Passwords don't match"        

    # Error if username or password has a space
    if ' ' in username:
        username_error = "That's not a valid username (no spaces allowed)"

    if ' ' in password:
        password_error = "That's not a valid password (no spaces allowed)"

    # Email validation
    if email:
        if len(email) < 3 or len(email) > 20:
            email_error = "That's not a valid email (must be between 3-20 characters long)"

        if ' ' in email or '@' not in email or '.' not in email:
            email_error = "That's not a valid email"
    
    # Success!
    if not username_error and not password_error and not verify_password_error and not email_error:
      # if successful, redirect
      return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template('user_signup_form.html',
        username=username, username_error=username_error,
        password_error=password_error,
        verify_password_error=verify_password_error,
        email=email, email_error=email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template("welcome_form.html", username=username)

app.run()
