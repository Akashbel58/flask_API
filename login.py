
from flask import Flask,render_template,request

app = Flask(__name__)

#  render_template for directing html file  
@app.route('/')
def index():
    return render_template('login.html')

# we are creating login html page for login function
# Creating API from frontend
 
@app.route('/login', methods=['POST'])
def login():
    user_name = request.form['username']
    password = request.form['password']
    print(user_name,password)

    return '<h1> Login Credentials received..!! </h1>'

if __name__ == '__main__':
    app.run(debug=True)  




