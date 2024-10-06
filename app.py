from flask import Flask,request,render_template

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit',methods=['GET','POST'])
def submit ():
    if request.method == 'POST':
            name=request.form['name']
            email=request.form['email']
            return render_template('result.html',name=name,email=email)
    else:
        
        return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
    
        