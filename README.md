# NLP-Based-Toxic-Comment-Detection-System

## DETECTING & BLOCKING MALICIOUS COMMENTS USING AI

This project is an AI-powered system designed to automatically **detect and flag toxic comments** using Natural Language Processing (NLP) techniques. The goal is to make online platforms safer by identifying harmful or abusive language in user-generated content.

### Dataset

We use the [**Jigsaw Toxic Comment Classification Challenge**](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge) dataset from Kaggle.
It includes labeled comments across six categories:

* Toxic
* Severe toxic
* Obscene
* Threat
* Insult
* Identity hate

[**Dataset link**](https://drive.google.com/drive/folders/1h_VObqxmpH0K8bbA8pyJiANnlLJyXvbS?usp=drive_link)

### Features

* Text preprocessing: cleaning, tokenization, stop-word removal
* Evaluation of multiple classifiers (Logistic Regression, Naive Bayes, Random Forest)
* **Logistic Regression** selected for its superior accuracy
* Integrated web interface to demo the system
* Scalable for future moderation tool integrations

### Installation

Install [**Tesseract OCR**](https://github.com/tesseract-ocr/tesseract) if OCR from images is needed:

installation path: C:\Program Files\Tesseract-OCR

```bash
sudo apt install tesseract-ocr
```

### Web Interface

Includes a lightweight web interface (Flask) to input image and displays flagged or toxic comments.


