from flask import Flask, request, jsonify
from flask_cors import CORS
from PyPDF2 import PdfReader
import pickle
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

# 🔹 Load trained ML model
with open("model.pkl", "rb") as f:
    vectorizer, job_vectors, job_titles = pickle.load(f)

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    
    if "resume" not in request.files:
        return jsonify({"error": "No resume uploaded"}), 400

    file = request.files["resume"]
    reader = PdfReader(file)

    
    resume_text = ""
    for page in reader.pages:
        if page.extract_text():
            resume_text += page.extract_text().lower()

    resume_vector = vectorizer.transform([resume_text])

 
    similarities = cosine_similarity(resume_vector, job_vectors)[0]

    
    results = []
    for i in range(len(job_titles)):
        results.append({
            "job": job_titles[i],
            "match": int(similarities[i] * 100)
        })

    
    results = sorted(results, key=lambda x: x["match"], reverse=True)

    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
