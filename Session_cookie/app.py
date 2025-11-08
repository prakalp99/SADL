from flask import Flask, request, session, redirect, url_for, render_template_string

app = Flask(__name__)
app.secret_key = 'replace_this_with_a_secret_key'  # Needed for session encryption

# Simple user data for demonstration
USERS = {'admin': 'password123'}

# Login Page & Form Handler
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USERS and USERS[username] == password:
            session['user'] = username  # Set session cookie
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials! <a href='/'>Try again</a>"

    # If already logged in, redirect to dashboard
    if 'user' in session:
        return redirect(url_for('dashboard'))

    return render_template_string(open('login.html').read())

# Dashboard (Protected Route)
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template_string(open('dashboard.html').read(), user=session['user'])
    return redirect(url_for('login'))

# Logout Handler
@app.route('/logout')
def logout():
    session.pop('user', None)  # Clear session cookie
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)