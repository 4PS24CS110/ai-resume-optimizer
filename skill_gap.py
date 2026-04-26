def extract_skills(text):
    skills_list = [
        "python", "sql", "machine learning", "react", "node",
        "java", "c", "c++", "data structures", "algorithms"
    ]

    text = text.lower()

    return [s for s in skills_list if s in text]


def get_skill_gap(resume, job_desc):
    resume_skills = extract_skills(resume)
    job_skills = extract_skills(job_desc)

    missing = list(set(job_skills) - set(resume_skills))

    return resume_skills, missing