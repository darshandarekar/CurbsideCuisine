from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection details
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1999",
  database="curbsidecuisine"
)

# login page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # get username and password from form
        username = request.form['username']
        password = request.form['password']
        
        # check if username and password match in database
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        if user is None:
            error = 'Invalid username or password'
        else:
            # redirect to success page
            return redirect(url_for('success'))
    return render_template('login.html', error=error)

# success page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run()
