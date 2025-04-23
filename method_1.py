
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Default API </h1>'

# Creating API from POSTMAN app 
# (we are not creating front for it = html page) 

@app.route('/getdata',methods = ['GET','POST'])
def getdata():
    if request.method == 'POST':
        # data = request.form.get('var') `              # another syntax access individual data
        data = request.form['var']                      #user input  #pass these arg to postman app
        print('\nData send from user : ',data)
        print(f'Type of data:{type(data)}\n')  
        return f'<h1> POST METHOD: Data received : {data} </h1>'
    else:
        return 'GET Method: Data not received'

# jsonify 
@app.route('/data', methods =['GET','POST'])
def data():
    if request.method == 'POST':
        data = request.form                           # user input in dict format
        print('\nData User Input: ',data)
        print(f'Type of data:{type(data)}\n')

        d1 = {'data':data} 
        return jsonify( d1)

    else:
        return 'GET Method: Data not received'

# get_json
@app.route('/json_data',methods = ['POST'])

def json_data():
    # data = request.json  # similar as get_json()
    data = request.get_json()
    print('\nJson_data: ',data)
    print(f'Type of data:{type(data)}\n')
    # return 'Json_data received..!!'
    return data

# Query_params
#  try to map URL and Fun_Name must be same

@app.route('/params',methods = ['POST'])
def params():
    data = request.args                          # for query_params in postman
    print('Query_Data: ',data)
    print(f'Type of data:{type(data)}\n')    
    # return 'Query_data received..!!'
    return data

if __name__ == '__main__':
    app.run(debug=True)