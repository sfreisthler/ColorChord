from flask import Flask, request, jsonify, send_file
from image_to_sound import image_to_sound
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

    try:
        image_to_sound(file)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    ####### PROCESS IMAGE HERE #############################

    return jsonify({'message': f"Processed {file.filename}"})


@app.route('/sound', methods=['GET'])
def send_sound():
    return send_file('./output.mp3', mimetype='audio/mp3')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 50000)) 
    app.run(host='0.0.0.0', port=port)

