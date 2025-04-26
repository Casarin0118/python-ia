from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

# Carrega a chave de API do arquivo .env
GEMINI_API_KEY = os.getenv('API')

# Verifica se a chave de API foi configurada
if not GEMINI_API_KEY:
    raise ValueError("A chave de API do Gemini não foi configurada no arquivo .env")

# Configura a API do Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')  # Use 'gemini-pro' para texto

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    prompt = request.args.get('prompt')

    if not prompt:
        return jsonify({'error': 'Nenhum prompt fornecido'}), 400

    context = 'Responda como se fosse uma inteligência artificial chamada Pedro'
    input_ia = f'{context}: {prompt}'  # Melhor formatação do prompt
    try:
        response = model.generate_content(input_ia)
        return jsonify({'message': response.text})
    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro na geração da resposta: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
