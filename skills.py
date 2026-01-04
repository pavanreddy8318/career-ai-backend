SKILLS_DB = {
    "python": "Data Scientist / Python Developer",
    "java": "Software Engineer",
    "aws": "Cloud Engineer",
    "machine learning": "AI / ML Engineer",
    "sql": "Data Analyst"
}

def match_skills(text):
    text = text.lower()
    matches = []

    for skill, job in SKILLS_DB.items():
        if skill in text:
            matches.append(job)

    if not matches:
        return ["No strong match found"]

    return list(set(matches))
JOB_SKILLS = {
    "Software Engineer": ["java", "python", "dsa"],
    "Data Scientist": ["python", "sql", "machine learning"],
    "Cloud Engineer": ["aws", "linux", "devops"]
}

def job_match_percentage(text):
    text = text.lower()
    results = []

    for job, skills in JOB_SKILLS.items():
        matched = [s for s in skills if s in text]
        percentage = int((len(matched) / len(skills)) * 100)

        results.append({
            "job": job,
            "match": percentage,
            "matched_skills": matched
        })

    return results
