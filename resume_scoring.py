
def score_resume(text):
    feedback = []
    section_scores = { 'About Me': 0, 'Education': 0, 'Experience': 0, 'Skills': 0, 'Certifications': 0 }
    keywords = ['Financial Statement', 'Tax', 'Compliance', 'Leadership', 'Teamwork', 'Budget', 'Forecast']

    for section in section_scores:
        if section.lower() in text.lower():
            section_scores[section] = 8
            feedback.append(f"{section}: Present. Score: 8/10")
        else:
            feedback.append(f"{section}: Missing or unclear. Score: 3/10")

    keyword_hits = [kw for kw in keywords if kw.lower() in text.lower()]
    feedback.append(f"Keyword Matches: {len(keyword_hits)} out of {len(keywords)}")

    if "coordinating" in text and "liaisoning" in text:
        feedback.append("Grammar: Correct spellings used.")
    else:
        feedback.append("Grammar: Issues found in spellings. Check 'coordinating' and 'liaisoning'.")

    overall_score = sum(section_scores.values()) // len(section_scores)
    feedback.insert(0, f"Overall Resume Score: {overall_score}/10")
    return "\n".join(feedback)
