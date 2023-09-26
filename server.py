from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='model_files')
CORS(app)

@app.route('/model_files/<path:filename>')
def serve_model(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(port=8080)
