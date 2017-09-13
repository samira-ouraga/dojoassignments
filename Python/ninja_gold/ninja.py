from flask import Flask, render_template, request, redirect, session,flash
import random
import time
import datetime

app = Flask(__name__)
app.secret_key = 'secretkey'

def randoming():
    session['point'] = random.randint(0,100)
    print session['point']

def playedat():
    session['when'] = datetime.datetime.now()
    print session['when']

@app.route('/')
def index():
    if 'point' not in session:
        randoming()
    else:
        pass
    print session['point']
    if 'when' not in session:
        playedat()
    else:
        pass
    print session['when']
    if 'total' not in session:
        session['total'] = 0
    else:
        session['total'] += session['point']
        print session['total']
    if 'activity' not in session:
        print("PUTTING ACTIVITIESIN SESSION")
        session['activity'] = []
    return render_template('index.html', total= session['total'], activities=session['activity'])

def selecting(name,point,when):
    if name == 'farm':
        print("FARMING!!!!")
        print(session['activity'])
        session['activity'].append('In the farm , you earned {} golds at {}'.format(session['point'],session['when']))
    elif name == 'cave':
        session['activity'].append('In the cave, you earned {} golds at {}'.format(session['point'],session['when']))
    elif name == 'house':
        session['activity'].append('In the house, you earned {} golds at {}'.format(session['point'],session['when']))
    elif name == 'casino':
        session['activity'].append('In the casino, you lost {} golds at {}'.format(session['point'],session['when']))
    else:
        print ('error')

@app.route('/process_money', methods = ['POST'])
def process():
    print(request.form)
    building = request.form['building']
    if building == 'farm':
        a = 10
        session['total'] += a
        selecting('farm', session['point'],session['when'])
    
    elif building == 'cave':
        b = 30
        session['total'] += b
        selecting('cave', session['point'],session['when'])

    elif building == 'house':
        c = 7
        session['total'] += c
        selecting('house', session['point'],session['when'])
    
    elif building == 'casino':
        d = 5
        session['total'] += d
        selecting('casino',session['point'],session['when'])

    else:
        print 'try again'

    return redirect('/')


@app.route('/clear' , methods=['POST'])
def clear():
    session.clear()
    return redirect('/')




app.run(debug=True)

#another way to display the messages
# class Message(object):
#   def __init__(self,what,moneys):
#       self.activity = activity
#       self.money = money  
#       self.time = datetime.datetime.now()
#       self.style = 'green' if moeny>= 0 else 'red'

#   def message(self):
#       return "aaaaa{} sssss {}".format(self.blb, self.bababab)

# if __name__ == '__main__' :
# bob = new Message('mine' , 15)
# print (bob,style) change 15 to -15 to get red text vis versa 
# print (bob, time)
# then in the corresponding route , session['activity'].append(Message('mine', num))
