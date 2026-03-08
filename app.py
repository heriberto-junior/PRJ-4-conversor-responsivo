from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Ativar CORS

# Diretório do projeto
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
COIN_PATH = os.path.join(PROJECT_DIR, 'coin')

@app.route('/converter', methods=['POST'])
def converter():
    """Converter moeda BRL para outra"""
    try:
        # Receber JSON
        data = request.get_json()
        if not data:
            return jsonify({'erro': 'JSON vazio', 'sucesso': False}), 400
        
        valor = str(data.get('valor', '')).strip()
        moeda = str(data.get('moeda', '')).strip().upper()
        
        # Validar
        if not valor or not moeda:
            return jsonify({'erro': 'Faltam parâmetros: valor e moeda', 'sucesso': False}), 400
        
        moedas_validas = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD']
        if moeda not in moedas_validas:
            return jsonify({'erro': f'Moeda inválida. Válidas: {", ".join(moedas_validas)}', 'sucesso': False}), 400
        
        logger.info(f"Convertendo: {valor} BRL → {moeda}")
        
        # Executar COBOL
        resultado = subprocess.run(
            [COIN_PATH, valor, moeda],
            capture_output=True,
            text=True,
            timeout=5,
            cwd=PROJECT_DIR
        )
        
        if resultado.returncode == 0:
            return jsonify({
                'resultado': resultado.stdout.strip(),
                'sucesso': True,
                'valor': valor,
                'moeda': moeda
            }), 200
        else:
            logger.error(f"Erro COBOL: {resultado.stderr}")
            return jsonify({'erro': resultado.stderr.strip(), 'sucesso': False}), 400
    
    except subprocess.TimeoutExpired:
        return jsonify({'erro': 'Timeout na execução', 'sucesso': False}), 408
    except Exception as e:
        logger.error(f"Erro: {str(e)}", exc_info=True)
        return jsonify({'erro': str(e), 'sucesso': False}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({
        'status': 'online',
        'servico': 'Conversor de Moedas COBOL',
        'versao': '1.0'
    }), 200

@app.route('/', methods=['GET'])
def home():
    """Home page com informações"""
    return jsonify({
        'nome': 'Conversor de Moedas',
        'desenvolvedor': 'Heriberto Mainframe Developer',
        'descricao': 'API REST que converte BRL para outras moedas usando COBOL',
        'endpoints': {
            'POST /converter': 'Converter moeda',
            'GET /health': 'Verificar status',
            'GET /': 'Informações da API'
        },
        'moedas_suportadas': ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD']
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
