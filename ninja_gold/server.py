from flask import Flask,render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'Baboo'
import random

def random_gems(num1, num2):
    gems = random.randint(num1, num2)
    return gems



@app.route('/')
def index():
    #session.clear()
    max_gems = 100
    if 'gems' not in session:
        session['gems'] = 0
    return render_template("mining.html", max_gems = max_gems)


#EXAMPLE OF USING PRINT STATEMENTS TO CHECK WORK
# @app.route('/process_gems', methods = ['POST'])
# def process_gems():
#     print(request.form['mines'])
#     return redirect('/')


#In this code use
#print(session['gems']) to see the results printed to the terminal
@app.route('/process_gems', methods = ['POST'])
def process_gems():
    if request.form['mines'] == 'sapphire':
        mined_gems = random_gems(5,10)
        session['gems'] += mined_gems
        print(session['gems'])

    if request.form['mines'] == 'ruby':
        mined_gems = random_gems(15,20)
        session['gems'] += mined_gems
        print(session['gems'])

    if request.form['mines'] == 'diamond':
        mined_gems = random_gems(2,5)
        session['gems'] += mined_gems
        print(session['gems']) 
    
    if request.form['mines'] == 'emerald':
        mined_gems = random_gems(-50,50)
        if mined_gems < 0:
            print("Run! It's going to BLOW!!!")
        session['gems'] += mined_gems
        print(session['gems']) 
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)

