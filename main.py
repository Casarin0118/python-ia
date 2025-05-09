from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

# Configura a API do Gemini
genai.configure(api_key=AIzaSyCHCgeKxkdlVzGzE72-xRI12AuQojG0pp0)
model = genai.GenerativeModel('gemini-2.0-flash')  # Use 'gemini-pro' para texto

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
        print(f"Enviando prompt para a API: {input_ia}")  # Log do prompt enviado
        response = model.generate_content(input_ia)
        print(f"Resposta completa da API: {response}")  # Log da resposta completa
        print(f"Texto da resposta da API: {response.text}")  # Log do texto da resposta
        return jsonify({'message': response.text})
    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")  # Log do erro
        return jsonify({'error': f'Ocorreu um erro na geração da resposta: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
