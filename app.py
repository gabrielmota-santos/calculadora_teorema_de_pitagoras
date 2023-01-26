from flask import Flask, render_template, url_for, make_response, request, redirect
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['GET', 'POST'])
def calcular():

    #COLETANDO OS DADOS DO FORMULARIO HTML.
    if request.method == 'POST':
        valorx = request.form.get('valorx')
        valory = request.form.get('valory')

    #CONVERTENDO OS TEXTOS EM FLOAT.
        valorx = float(valorx)
        valory = float(valory)

    #VALOR DA HIPOTENUSA AO QUADRADO
        hipotenusa = (valorx * valorx) + (valory * valory)

    #ACHANDO A RAIZ QUADRADA DA HIPOTENUSA.
        hipotenusa = math.pow(hipotenusa, 1/2)

        hipotenusa = f'{hipotenusa:.2f}'

    #CHAMANDO O index.html, E PASSANDO O VALOR DO PARÂMETRO.
        return render_template('index.html', hipotenusa=hipotenusa)
