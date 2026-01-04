import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# 1️⃣ Load dataset
df = pd.read_csv("jobs.csv")

# 2️⃣ Train TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["description"])

# 3️⃣ Save trained model
with open("model.pkl", "wb") as f:
    pickle.dump((vectorizer, X, df["job_title"].tolist()), f)

print("✅ Model trained and saved as model.pkl")
