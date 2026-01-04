from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Job descriptions (training data)
JOB_DATA = {
    "Software Engineer": "java python dsa algorithms oops coding",
    "Data Scientist": "python sql machine learning statistics data analysis",
    "Cloud Engineer": "aws linux devops docker kubernetes cloud"
}

def match_resume_ml(resume_text):
    documents = [resume_text] + list(JOB_DATA.values())

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    resume_vector = tfidf_matrix[0]
    job_vectors = tfidf_matrix[1:]

    similarities = cosine_similarity(resume_vector, job_vectors)[0]

    results = []
    for i, job in enumerate(JOB_DATA.keys()):
        results.append({
            "job": job,
            "match": int(similarities[i] * 100)
        })

    return sorted(results, key=lambda x: x["match"], reverse=True)
