from flask import Flask, request, jsonify, send_from_directory, abort
import os
import random
import string
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)


SECRET_KEY = os.getenv("SECRET_KEY")
SHAREX_DIR = os.getenv("DIR")
DOMAIN_URL = os.getenv("DOMAIN_URL")
LENGTH_OF_STRING = os.getenv("STRING_LEN")

def random_string(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for i in range(length))


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'secret' not in request.form:
        return 'No post data received', 400

    secret = request.form['secret']
    if secret != SECRET_KEY:
        return 'Invalid Secret Key', 403

    if 'sharex' not in request.files:
        return 'No file uploaded', 400

    file = request.files['sharex']
    filename = random_string(LENGTH_OF_STRING)
    file_ext = os.path.splitext(file.filename)[1]
    save_path = os.path.join(SHAREX_DIR, filename + file_ext)

    try:
        file.save(save_path)
        file_url = DOMAIN_URL + SHAREX_DIR + filename + file_ext
        return file_url
    except Exception as e:
        return f'File upload failed - {str(e)}', 500

@app.route('/images/<filename>', methods=['GET'])
def get_image(filename):
    try:
        return send_from_directory(SHAREX_DIR, filename)
    except FileNotFoundError:
        abort(404, description="Image not found")

@app.route('/', methods=['GET'])
def default_page():
    return jsonify({"message": "Images Server Live!"})

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not Found'}), 404

if __name__ == '__main__':
    if not os.path.exists(SHAREX_DIR):
        os.makedirs(SHAREX_DIR)
    app.run(debug=True, host='127.0.0.1', port=5000)
