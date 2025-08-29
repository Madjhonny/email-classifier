import os
import requests
import fitz 
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

HF_API_KEY = os.getenv("HF_API_KEY")
HF_API_URL_CLASSIFICATION = "https://api-inference.huggingface.co/models/valhalla/distilbart-mnli-12-3"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}


def extract_text_from_pdf(pdf_stream):
    """Lê um fluxo de bytes de um PDF e retorna seu texto."""
    try:
        with fitz.open(stream=pdf_stream, filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            return text
    except Exception as e:
        print(f"Erro ao extrair texto do PDF: {e}")
        return "" 

def classify_text(text):
    """Envia o texto para a API da Hugging Face e retorna a classificação."""
    payload = {
        "inputs": text,
        "parameters": {"candidate_labels": ["produtivo", "improdutivo"]},
    }
    try:
        response = requests.post(HF_API_URL_CLASSIFICATION, headers=headers, json=payload, timeout=60)
        response.raise_for_status() 
        return response.json()['labels'][0]
    except requests.exceptions.RequestException as e:
        print(f"Erro na chamada da API: {e}")
        return "indefinido" 

@app.route('/')
def index():
    """Renderiza a página inicial (nosso index.html)."""
    return render_template('index.html')

@app.route('/processar-pdfs', methods=['POST'])
def processar_pdfs():
    """Recebe os arquivos PDF, classifica e retorna a lista priorizada."""
    uploaded_files = request.files.getlist('pdfs')
    
    if not uploaded_files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    results = []
    for pdf_file in uploaded_files:
        if pdf_file.filename != '':
            pdf_bytes = pdf_file.read()
            email_text = extract_text_from_pdf(pdf_bytes)
            
            if not email_text.strip():
                classification = "improdutivo" 
            else:
                classification = classify_text(email_text)

            results.append({
                "filename": pdf_file.filename,
                "category": classification.capitalize() 
            })
    
    
    prioritized_results = sorted(results, key=lambda x: x['category'] == 'Produtivo', reverse=True)
    
    return jsonify(prioritized_results)


if __name__ == '__main__':
    app.run(debug=True)