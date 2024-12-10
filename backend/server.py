from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    ####### PROCESS IMAGE HERE #############################

    return jsonify({'message': f"Processed {file.filename}"})


@app.route('/sound', methods=['GET'])
def send_sound():
    return send_file('../static/beer_soda_crack_open_can_fizz_2.wav', mimetype='audio/wav')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 50000)) 
    app.run(host='0.0.0.0', port=port)

