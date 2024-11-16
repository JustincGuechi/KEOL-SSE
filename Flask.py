from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'xlsx', 'xls'}
JSON_FOLDER = 'json'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_FOLDER'] = JSON_FOLDER


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

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
        return jsonify({"message": "File successfully uploaded and renamed", "filename": new_filename}), 200

    return jsonify({"error": "File type not allowed"}), 400

@app.route('/getjson', methods=['GET'])
def get_json():
    year = request.args.get('year', type=int)
    month = request.args.get('month', type=int)
    day = request.args.get('day', type=int)

    if not all([year, month, day]):
        return jsonify({"error": "Missing date parameters"}), 400

    json_filename = f"{year}_{month}_{day}.json"
    print(json_filename)
    json_filepath = os.path.join(app.config['JSON_FOLDER'], json_filename)

    if not os.path.exists(json_filepath):
        return jsonify({"error": "File not found"}), 404

    with open(json_filepath, 'r') as json_file:
        data = json.load(json_file)

    return jsonify(data), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
