from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def getUser(name):
    return render_template('user.html', name=name)

@app.route('/galeria')
def galeria():
    lista = [
        'https://goo.gl/KHgEBr',
        'https://goo.gl/W2H35k',
        'https://goo.gl/9qAnVL',
        'https://goo.gl/vi5Hc5'
    ]
    
    return render_template('galeria.html', lista = lista)
