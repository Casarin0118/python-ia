from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import generativeai as genai
import os

load_dotenv()

# Configurar API antes de instanciar o modelo
genai.configure(api_key=os.getenv('API'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    context = 'Responda como se fosse uma inteligência artificial chamada Pedro'
    prompt = request.args.get('prompt')
    
    if not prompt:
        return {'error': 'Nenhum prompt fornecido'}, 400  # Retorna erro 400 se não houver prompt

    input_ia = f'{context} : {prompt}'
    output = model.generate_content(input_ia)
    
    return {'message': output.text}

if __name__ == '__main__':
    app.run(debug=True)