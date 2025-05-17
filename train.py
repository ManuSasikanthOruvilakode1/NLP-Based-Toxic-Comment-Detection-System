import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.exceptions import UndefinedMetricWarning
import joblib
import warnings

model_path = "*** file path ***/Malicious_Comment_Detector.pkl"
CONFIDENCE_THRESHOLD = 0.75

def train_model():
    df = pd.read_csv("*** file path ***/train.csv")

    # Drop any unnamed index columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # ====== VISUALIZATIONS ======
    target_cols = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

    # Class Distribution
    class_counts = df[target_cols].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=class_counts.index, y=class_counts.values, palette="viridis")
    plt.title("Distribution of Malicious Comment Classes")
    plt.ylabel("Number of Comments")
    plt.xlabel("Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Comment Length Distribution
    df['comment_length'] = df['comment_text'].apply(lambda x: len(str(x).split()))
    plt.figure(figsize=(10, 6))
    sns.histplot(df['comment_length'], bins=50, kde=True)
    plt.title("Distribution of Comment Lengths (in words)")
    plt.xlabel("Number of Words")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # Correlation Heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(df[target_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Between Malicious Comment Labels")
    plt.tight_layout()
    plt.show()

    # ====== VISUALIZATIONS END ======

    # Spliting data
    X = df['comment_text']
    y = df[target_cols]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # For classifier comparision
    classifiers = {
        "Logistic Regression": LogisticRegression(max_iter=200),
        "Multinomial Naive Bayes": MultinomialNB(),
        "Random Forest": RandomForestClassifier(n_estimators=100, n_jobs=-1)
    }

    results = {}

    for name, clf in classifiers.items():
        print("\n ======================================")
        print(f"\nTraining model: {name}")
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(stop_words='english', max_df=0.9)),
            ('clf', OneVsRestClassifier(clf))
        ])
        pipeline.fit(X_train, y_train)

        # Applying confidence threshold for prediction
        y_probs = pipeline.predict_proba(X_test) 
        y_pred = (y_probs >= CONFIDENCE_THRESHOLD).astype(int)

        #print  the accuracy score
        acc = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {acc:.4f}")

        # Remove warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=UndefinedMetricWarning)
            print("Classification Report:")
            print(classification_report(y_test, y_pred, target_names=target_cols, zero_division=0))

        results[name] = {
            "model": pipeline,
            "accuracy": acc
        }

    # PRINT ALL ACCURACIES
    print("\n======= Model Accuracy Summary ======")
    for model_name, info in results.items():
        print(f"{model_name}: {info['accuracy']:.4f}")

    # Select and display best model
    best_model_name = max(results, key=lambda k: results[k]["accuracy"])
    best_model = results[best_model_name]["model"]
    best_accuracy = results[best_model_name]["accuracy"]
    print(f"\nSelected Best Model: {best_model_name} with Accuracy: {best_accuracy:.4f}")
    
    # Saved the best model
    joblib.dump(best_model, model_path)
    print(f"Model saved to: {model_path}")

if __name__ == "__main__":
    train_model()
