from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import requests

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'xlsx', 'xls'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Endpoint de test
@app.route('/', methods=['GET'])
def read_root():
    return "Bienvenue sur l'API KEOLÏSSE"

@app.route('/upload', methods=['POST'])
def upload_file():



    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Récupérer le paramètre filename depuis la requête
    custom_filename = request.form.get('filename')
    if  custom_filename and any(char.isalpha() for char in custom_filename):
        new_filename = f"{custom_filename}.pdf"
    else :
        new_filename = f"renamed_{file.filename}"

    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
        return jsonify({"message": "File successfully uploaded and renamed", "filename": new_filename}), 200

    return jsonify({"error": "File type not allowed"}), 400

if __name__ == '__main__':
    app.run(debug=True)
