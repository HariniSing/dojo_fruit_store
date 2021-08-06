from flask import Flask, render_template, request, redirect
from datetime import datetime
now = datetime.now()
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    count = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print(f"charging {request.form['first_name']} {request.form['last_name']} for {count} fruits!")
    print(request.form)
    return render_template("checkout.html",first_name = request.form['first_name'], last_name = request.form['last_name'], id = request.form['student_id'],strawberry = request.form['strawberry'], raspberry = request.form['raspberry'], apple = request.form['apple'], count = count, time = now)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    