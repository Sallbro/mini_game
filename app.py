from flask import *  

app = Flask(__name__)  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Add_money')  
def Add_money():  
    return render_template('./Add_money/index.html') 

@app.route('/calculator')  
def calculator():  
    return render_template('./calculator/calculator.html')

@app.route('/dino')  
def dino():  
    return render_template('./dino/index.html')

@app.route('/library-project')  
def library():  
    return render_template('./library-project/index.html')
 
@app.route('/memory_match')  
def memory_match():  
    return render_template('./memory_match/index.html') 

@app.route('/note_making')  
def note_making():  
    return render_template('./note_making/index.html')

@app.route('/snake')  
def snake():  
    return render_template('./snake/index.html')

@app.route('/subway_suffer')  
def subway_suffer():  
    return render_template('./subway_suffer/index.html')

@app.route('/tic_tac_toe')  
def tic_tac_toe():  
    return render_template('./tic_tac_toe/index.html')
 
@app.route('/todo_list')  
def todo_list():  
    return render_template('./todo_list/index.html')   
  





if __name__ =='__main__':  
    app.run(debug = True)  