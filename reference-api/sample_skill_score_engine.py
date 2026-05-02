"""
Sanitized reference skill score engine for SkillNyx.

This file is for portfolio demonstration only.
It does not include production SkillNyx source code, database schema,
billing logic, AI prompts, user data, or proprietary scoring logic.
"""


def calculate_skill_score(assessment_score, coding_score, learning_progress):
    """
    Calculates a simplified skill score using sanitized reference weights.
    """

    weights = {
        "assessment": 0.40,
        "coding": 0.40,
        "learning": 0.20,
    }

    score = (
        assessment_score * weights["assessment"]
        + coding_score * weights["coding"]
        + learning_progress * weights["learning"]
    )

    return round(score, 2)


def classify_skill_level(score):
    if score >= 85:
        return "Advanced"
    if score >= 70:
        return "Intermediate"
    if score >= 50:
        return "Foundational"
    return "Needs Improvement"


if __name__ == "__main__":
    skill_score = calculate_skill_score(
        assessment_score=84,
        coding_score=79,
        learning_progress=91,
    )

    print({
        "skillScore": skill_score,
        "skillLevel": classify_skill_level(skill_score),
    })
