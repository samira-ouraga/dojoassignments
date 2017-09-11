from flask import Flask, render_template, request, redirect, session,flash
import random 

app = Flask(__name__)
app.secret_key = 'secretkey'

def randoming():
    session['other'] = random.randint(0,100)

@app.route('/')
def index():
    if session['other'] == None:
        randoming()
    else:
        pass
    print session['other']
    return render_template('index.html')


@app.route('/high', methods = ['POST'])
def high():  
    number = request.form['number']
    if request.method == 'POST':
        if number.isdigit():
            choice = int(number)
            if  choice == session['other']:
                flash ('correct')
                return redirect('/')
            
            elif choice > session['other']:
                flash ('too high')

            else:
                flash ('too low')
        else:
            flash('write a number')
    else:
        flash('not a good guess')
    return redirect('/')

@app.route('/clear', methods=['POST'])
def reset():
    randoming()
    return redirect('/')
    

app.run(debug=True)   