# NLP-Based-Toxic-Comment-Detection-System

Sure! Here’s your updated **GitHub repository description** with the **Jigsaw Toxic Comment Classification Challenge** properly named and linked:

---

## 🧠 NLP-Based Toxic Comment Detection System

### 🔒 DETECTING & BLOCKING MALICIOUS COMMENTS USING AI

This project is an AI-powered system designed to automatically **detect and flag toxic comments** using Natural Language Processing (NLP) techniques. The goal is to make online platforms safer by identifying harmful or abusive language in user-generated content.

---

### Dataset

We use the [**Jigsaw Toxic Comment Classification Challenge**](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge) dataset from Kaggle.
It includes labeled comments across six categories:

* Toxic
* Severe toxic
* Obscene
* Threat
* Insult
* Identity hate

---

### Features

* Text preprocessing: cleaning, tokenization, stop-word removal
* Evaluation of multiple classifiers (Logistic Regression, SVM, etc.)
* **Logistic Regression** selected for its superior accuracy
* Integrated web interface to demo the system
* Scalable for future moderation tool integrations

---

### 🛠️ Installation

```bash
git clone https://github.com/your-username/toxic-comment-detector.git
cd toxic-comment-detector
pip install -r requirements.txt
```

Install [**Tesseract OCR**](https://github.com/tesseract-ocr/tesseract) if OCR from images is needed:

```bash
sudo apt install tesseract-ocr
```

---

### 🌐 Web Interface

Includes a lightweight web interface (Streamlit/Flask) to input or test comments and receive toxicity classification in real time.


