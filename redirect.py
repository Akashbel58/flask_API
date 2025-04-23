
from flask import Flask,url_for,redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1> Default page </h1>'

@app.route('/admin')
def admin_name():
    return '<h1> This is admin </h1>'

@app.route('/greet/<name>')
def greet_msg(name):
    return f'<h1> Hello {name} Welcome to Flask </h1>'

# redirect to another API / webpage
@app.route('/user/<input>')
def user(input):
    if input == 'admin':
        return redirect(url_for('admin_name'))
    else:
        return redirect(url_for('greet_msg',name=input))

# syntax 1:
# app.run(debug=True)

# syntax 2:

if __name__ == '__main__':
    app.run(debug=True)

#  syntax 3: from CMD
# set FLASK_APP=hello   
#  flask run