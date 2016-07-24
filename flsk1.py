'''from flask import Flask
app = Flask("sravani")

@app.route('/')
def hi():    #did not pass any argument in route so not defined in fn
    return 'good evening'
app.run(port=5252)'''




'''from flask import Flask 
app = Flask(__name__) 
@app.route('/hello/<guest>')    #to change name dynamically on the url(use name,guest)
def hi(guest): #must define argument which u write in route will define in function
  return 'hi %s is an employee' % guest
  return 'Hello %s is an employee' % guest
#if __name__ == '__main__': 
app.run(debug=True)'''




'''from flask import Flask 
app = Flask(__name__) 
@app.route('/sravani/<int:sravs>') #to accept integer
def show_hi(sravs): 
    return 'sravanis %d' % sravs
@app.route('/pandu/<float:revNo>') #to accept floating point
def revision(revNo): 
    return 'pandu %f' % revNo 
if __name__ == '__main__': 
    app.run()'''





'''from flask import Flask 
app = Flask(__name__) 
@app.route('/flask') 
def hello_flask(): 
    return 'Hello Flask'   # flask doesnot support slash ie /flask/ like this
@app.route('/python/') 
def hello_python(): 
    return 'Hello Python' 
if __name__ == '__main__': 
    app.run()'''



'''from flask import Flask
app = Flask(__name__)
@app.route('/abc')
def h():
    return 'hi gud mng'
@app.route('/abc/<name>')
def h1(name):                                    #did not condition 14th
    return 'hi %s act smart' %name
@app.route('/user/<name>')
def h2_user(name):
   if name == 'abc':
      return (url_for('h'))
   else:
       return redirect(url_for('h1', name=name))
#if __name__ == '__main__':                            
       app.run()'''






'''from flask import Flask 
app = Flask(__name__) 
@app.route('/sravs') 
def index(): 
    return '<html><body><h1>Hello World </h1></body><html>' 
if __name__ == '__main__': 
    app.run(debug=True) '''


'''from flask import Flask 
app = Flask(__name__) 
@app.route('/') 
def index(): 
    return render_template(‘hello.html’)   
if __name__ == '__main__': 
    app.run(debug=True)''' 


'''from flask import Flask,redirect,url_for
app = Flask(__name__)
@app.route('/admin')
def hi_admin():
    return 'hi sravani'
@app route('/guest/<guest>')
def hi_guest(guest):
    return 'hi %s as guest' % guest
@app.route('/user/<name>')
def hi_user(name):
    if name =='admin':
        return redirect(url_for('hi_admin'))
    else:
        return redirect(url_for('hi guest',guest==name))
if __name__ =='__main__':    
     app.run(debug=True)'''
    
from flask import Flask,redirect,url_for,request
app = Flask(name)
@app.route('/hi/<name>')
def hello(name):
    return 'hello %s' %name
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method =="POST":
        user=request.form['nm']
        return redirect(url_for('hi',name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('hi',name=user))
if__name__=='__main__':
    app.run(debug = True)

