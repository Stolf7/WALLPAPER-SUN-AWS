from flask import Flask, request, jsonify, render_template
import boto3
from botocore import UNSIGNED
from botocore.config import Config
import uuid
import datetime

app = Flask(__name__)

# Cliente S3 anônimo (sem autenticação)
s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

# Nome do bucket (já deve estar com política pública ativada)
bucket_name = 'wallpaper-sun-2025'

# Página inicial com formulário de upload
@app.route('/')
def index():
    return render_template('index.html')

# Galeria de imagens públicas do S3
@app.route('/gallery')
def gallery():
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        images = []

        if 'Contents' in response:
            for obj in response['Contents']:
                image_url = f"https://{bucket_name}.s3.amazonaws.com/{obj['Key']}"
                images.append(image_url)

        return render_template('gallery.html', images=images)
    
    except Exception as e:
        return f"Erro ao carregar as imagens: {str(e)}"

# Rota de upload
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Nenhum arquivo enviado'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'Nenhum arquivo selecionado'}), 400

        filename = f"{uuid.uuid4()}_{file.filename}"  # evita arquivos com o mesmo nome
        s3.upload_fileobj(file, bucket_name, filename)

        url = f"https://{bucket_name}.s3.amazonaws.com/{filename}"
        print(f"[LOG] Imagem enviada com sucesso: {url}")

        return jsonify({
            'message': 'Upload realizado com sucesso!',
            'url': url
        }), 200

    except Exception as e:
        print(f"[ERRO] Falha ao enviar imagem: {str(e)}")
        return jsonify({'error': f'Erro no upload: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
