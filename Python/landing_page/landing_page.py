from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    the_ninjas = ['Ninja Gold', 'Great Number Game', 'Disappearing Ninjas', 'Dojo Survey']
    return render_template('ninjas.html', ninjas=the_ninjas)

@app.route('/dojo')
def dojo():
    return render_template('dojo.html')

app.run(debug=True)