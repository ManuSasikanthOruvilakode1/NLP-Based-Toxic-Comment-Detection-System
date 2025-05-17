# NLP-Based-Toxic-Comment-Detection-System
🧠 NLP-Based Toxic Comment Detection System
🔒 DETECTING & BLOCKING MALICIOUS COMMENTS USING AI
This project is an AI-powered system designed to automatically detect and flag toxic comments using Natural Language Processing (NLP) techniques. The primary goal is to make online platforms safer by identifying harmful content in user-generated text.

📊 Dataset
The model is trained using the Jigsaw Toxic Comment Classification Challenge dataset, which contains labeled comments categorized as toxic, severe toxic, obscene, threat, insult, and identity hate.

🚀 Features
Preprocessing of raw text (tokenization, stop word removal, etc.)

Comparison of multiple classifiers (Logistic Regression, SVM, etc.)

Final model uses Logistic Regression due to its high accuracy

Web interface to simulate real-world usage and flag toxicity

Easy integration for future moderation tools

🛠️ Installation
Clone the repository and install required packages:

bash
Copy
Edit
git clone https://github.com/your-username/toxic-comment-detector.git
cd toxic-comment-detector
pip install -r requirements.txt
Make sure to install Tesseract OCR if your pipeline includes text extraction from images:

bash
Copy
Edit
sudo apt install tesseract-ocr
🌐 Web Interface
Includes a simple and interactive interface to test the model on sample comments or user input. Built using Streamlit/Flask (mention the one you used).
