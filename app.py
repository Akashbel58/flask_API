from flask import Flask

app = Flask(__name__)
print('print app: ',app)

@app.route('/')
def hello():
    return '<h1> Default page </h1>'

@app.route('/about')
def about():
    return '<h1> This is about page..!!</h1>'

@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello {name} Welcome to Flask</h1>'

if __name__ == '__main__':
    app.run(debug=True)





