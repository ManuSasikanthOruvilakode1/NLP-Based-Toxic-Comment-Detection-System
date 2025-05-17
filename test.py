import pandas as pd
import joblib
import re

# Load model
model_path = "*** file path ***/Malicious_Comment_Detector.pkl"
model = joblib.load(model_path)

# Define label names
LABELS = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

# Load test data
df = pd.read_csv("*** file path ***/test.csv")

# Check if 'text' column exists
if 'comment_text' not in df.columns:
    raise ValueError("Expected column 'text' not found in test.csv")

# Preprocess the text
df['clean_comment_text'] = df['comment_text'].astype(str).str.lower().apply(lambda x: re.sub(r'\s+', ' ', x.strip()))

# Predict
predictions = model.predict(df['clean_comment_text'])

# create output DataFrame
results = []
for i, row in enumerate(predictions):
    comment = df.loc[i, 'comment_text']
    predicted_labels = [label for label, val in zip(LABELS, row) if val == 1]
    if predicted_labels:  # Only include rows with at least one label predicted
        results.append({
            'comment_text': comment,
            'predicted_labels': ', '.join(predicted_labels)
        })

output_df = pd.DataFrame(results)

# Show top results
print(output_df.head(10))
