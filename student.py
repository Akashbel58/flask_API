
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('student.html')

@app.route('/student',methods = ['POST'])
def student():
    student_data = request.form       # how to iterrate data this data(student_data)    
    print('\nStudent_data: ',student_data)
    print(f'Type of data:{type(student_data)}\n')
    
    # data = {'data': student_data}
    # print(data)

    return 'Student data Received'
    # return render_template('student_info.html')

if __name__ == '__main__':
    app.run(debug=True)






  