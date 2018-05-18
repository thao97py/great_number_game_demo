from flask import Flask, render_template, request, redirect, session
import random
app=Flask(__name__)
app.secret_key = "ThisIsSecured"
@app.route('/')
def game_interface():
    if'out' not in session:
        session['out']=''
    return render_template('game.html', output=session['out'])

@app.route('/process', methods=['POST'])
def compare():
    num=random.randrange(0,101)
    print num
    guess=request.form['numbers']
    print guess
    if'out' not in session:
        session['out']=''
    
    if num<int(guess):
        result='Too High'
    elif num>int(guess):
        result = 'Too Low'
    else:
        result=num
    
    session['out']=result
    return redirect('/')

@app.route('/clear')
def session_clear():
    session.clear()
    return redirect('/')

@app.route('/restart')
def restart():
    session.pop('out')
    return redirect('/')

app.run(debug=True)