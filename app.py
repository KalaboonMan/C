from flask import Flask,render_template,request,url_for

app = Flask(__name__)

courses = [
    {'code': 'TH001', 'name': 'thai'},
    {'code': 'Eng002', 'name': 'english'},
    {'code': 'Ir003', 'name': 'Ir'},
]

@app.route('/')
def imdex():
    return render_template('index.html', courses = courses)

@app.route('/search_by_name', methods=['GET','POST'])
def search_by_name():
    result = None
    
    if request.method == 'POST':
        course_name = request.form.get('course_name')
        result = next((course for course in courses if course['name'] == course_name), None)
        
    return render_template('search_by_name.html', result=result)