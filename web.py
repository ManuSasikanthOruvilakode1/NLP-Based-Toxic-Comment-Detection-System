from flask import Flask, render_template_string, request
import pytesseract
from PIL import Image
import joblib
import os
import re
from werkzeug.utils import secure_filename

# Set path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load trained model from specific path
MODEL_PATH = "*** file path ***/Malicious_Comment_Detector.pkl"
LABELS = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

# Load model
model = joblib.load(MODEL_PATH)

# Web setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


# HTML interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Malicious Comment Detector</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background: #eef2f5;
            color: #333;
            text-align: center;
            padding: 2em;
        }
        h2 {
            color: #222;
        }
        form {
            background: white;
            padding: 2em;
            margin: auto;
            width: 90%;
            max-width: 400px;
            border-radius: 12px;
            box-shadow: 0 5px 10px rgba(0,0,0,0.1);
        }
        input[type="file"] {
            padding: 0.5em;
            margin: 1em 0;
        }
        input[type="submit"] {
            background: #0066cc;
            color: white;
            padding: 0.7em 1.2em;
            border: none;
            font-size: 1em;
            border-radius: 6px;
            cursor: pointer;
        }
        .result-section {
            margin-top: 2em;
        }
        .card {
            background: white;
            padding: 1.5em;
            margin: 1em auto;
            max-width: 600px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
        .labels span {
            display: inline-block;
            background: #ff6961;
            color: white;
            padding: 0.4em 0.8em;
            margin: 0.3em;
            border-radius: 15px;
            font-weight: bold;
        }
        .clean {
            color: green;
            font-weight: bold;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h2>Malicious Comment Detector</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="image" required>
        <br>
        <input type="submit" value="Detect">
    </form>

    {% if extracted_text %}
    <div class="result-section">
        <div class="card">
            <h3>Extracted Text</h3>
            <p>{{ extracted_text }}</p>
        </div>
        <div class="card">
            <h3>Detection Result</h3>
            {% if labels %}
                <div class="labels">
                    {% for label in labels %}
                        <span>{{ label }}</span>
                    {% endfor %}
                </div>
            {% else %}
                <p class="clean"> This comment is clean / neutral.</p>
            {% endif %}
        </div>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    extracted_text = None
    labels = []

    if request.method == "POST":
        file = request.files.get("image")
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            try:
                # OCR
                image = Image.open(filepath)
                extracted_text = pytesseract.image_to_string(image)
                
                # Clean and normalize text
                extracted_text = extracted_text.strip().lower()
                extracted_text = re.sub(r'\s+', ' ', extracted_text)
                print("Extracted text:", repr(extracted_text))

                if extracted_text:
                    # Predict
                    prediction = model.predict([extracted_text])[0]
                    print("Prediction:", prediction)
                    labels = [label for label, flag in zip(LABELS, prediction) if flag == 1]
                else:
                    extracted_text = "[No readable text detected]"
                    labels = []

            except Exception as e:
                extracted_text = f"[Error during processing: {e}]"
                labels = []

    return render_template_string(HTML_TEMPLATE, extracted_text=extracted_text, labels=labels)

@app.route("/shutdown", methods=["POST"])
def shutdown():
    func = request.environ.get("werkzeug.server.shutdown")
    if func:
        func()
    return "Shutting down..."

if __name__ == "__main__":
    print("Server running at http://127.0.0.1:5000/")
    app.run(debug=True)