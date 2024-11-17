from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    file_path = f"./uploads/{file.filename}"
    file.save(file_path)

    return jsonify({'message': f"Processed {file.filename}"})

if __name__ == '__main__':
    app.run(debug=True)
