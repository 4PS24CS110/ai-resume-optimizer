import streamlit as st
from resume_parser import extract_text
from ats_score import ats_score
from skill_gap import get_skill_gap
from resume_tailor import suggestions

st.title("🚀 AI Resume Optimizer")

file = st.file_uploader("Upload Resume (PDF)")
job_desc = st.text_area("Paste Job Description")

if file and job_desc:
    resume_text = extract_text(file)

    score, keywords = ats_score(resume_text, job_desc)
    found, missing = get_skill_gap(resume_text, job_desc)

    # 🎯 ATS SCORE
    st.subheader(f"ATS Score: {score}%")
    st.progress(score / 100)

    if score > 75:
        st.success("Strong match ✅")
    elif score > 50:
        st.warning("Average match ⚠️")
    else:
        st.error("Low match ❌ Improve your resume")

    # ✅ MATCHED KEYWORDS
    st.subheader("✅ Matched Keywords")
    for k in keywords:
        st.success(k)

    # ❌ MISSING SKILLS
    st.subheader("❌ Missing Skills")
    for m in missing:
        st.error(m)

    # 📊 SKILL GAP
    st.subheader("📊 Skill Gap Analysis")
    st.warning(f"You are missing {len(missing)} important skills")

    # ✨ SUGGESTIONS
    st.subheader("✨ Suggestions")
    st.write(suggestions(missing))