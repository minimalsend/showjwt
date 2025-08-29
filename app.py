from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/token', methods=['GET'])
def get_tokens():
    urls = [
        'https://scvirtual.alphi.media/botsistem/sendlike/token_br.json',
        'https://scvirtual.alphi.media/botsistem/sendlike/tokenbr.json'
    ]
    
    all_tokens = []
    
    try:
        for url in urls:
            response = requests.get(url)
            response.raise_for_status()
            
            tokens_data = response.json()
            # Garante que só pega 'token' se a chave existir
            for item in tokens_data:
                if 'token' in item:
                    all_tokens.append(item['token'])
        
        # Remove duplicados mantendo a ordem
        all_tokens = list(dict.fromkeys(all_tokens))
        
        return jsonify({"tokens": all_tokens})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
