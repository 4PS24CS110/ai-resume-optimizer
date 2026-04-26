stopwords = ["the", "a", "to", "and", "of", "in", "with", "for", "is", "we", "are"]

def ats_score(resume, job):
    resume_words = set(resume.lower().split())
    job_words = set(job.lower().split())

    job_words = {w for w in job_words if w not in stopwords and len(w) > 2}

    matched = resume_words.intersection(job_words)

    score = len(matched) / len(job_words) * 100

    return round(score, 2), list(matched)