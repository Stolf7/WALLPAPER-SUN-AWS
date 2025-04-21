from flask import Flask, request, jsonify, render_template
import boto3
from botocore import UNSIGNED
from botocore.config import Config
import uuid
import datetime

app = Flask(__name__)

# Cliente S3 anônimo
s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

# Bucket e nome da tabela
bucket_name = 'wallpaper-sun-2025'

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota galeria
@app.route('/gallery')
def gallery():
    try:
        # Lista os objetos (imagens) no S3
        response = s3.list_objects_v2(Bucket=bucket_name)
        images = []

        # Verifica se o bucket tem arquivos e os adiciona à lista de imagens
        if 'Contents' in response:
            for obj in response['Contents']:
                image_url = f"https://{bucket_name}.s3.amazonaws.com/{obj['Key']}"
                images.append(image_url)

        return render_template('gallery.html', images=images)

    except Exception as e:
        return f"Erro ao carregar as imagens: {str(e)}"


# Upload de imagem
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        filename = file.filename
        image_id = str(uuid.uuid4())
        now = datetime.datetime.utcnow().isoformat()

        # Upload para o S3
        s3.upload_fileobj(file, bucket_name, filename)

        url = f'https://{bucket_name}.s3.amazonaws.com/{filename}'

        # Retorno simples (sem DynamoDB)
        return jsonify({
            'message': 'Upload successful',
            'image_id': image_id,
            'filename': filename,
            'url': url
        }), 200

    except Exception as e:
        return jsonify({'error': f'Error uploading file to S3: {str(e)}'}), 500

# Lista básica (sem DynamoDB)
@app.route('/images', methods=['GET'])
def list_images():
    try:
        # Como não usamos DynamoDB, lista hardcoded (exemplo)
        return jsonify([])  # Ou você pode criar algo fixo só pra teste
    except Exception as e:
        return jsonify({'error': f'Error listing images: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')