from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print "Got Post Info"
    # recall the name attributes we added to our form inputs
    # to access the data that the user input into the fields we use request.form['name_of_input']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    print request.form
    return render_template('process.html') #this to go to second page or do return redirect('/') redirects back to the '/' route
    

app.run(debug=True)