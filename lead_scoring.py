def score_lead(phone, email, website):

    score = 0

    if phone:
        score += 30

    if email != "Not Found":
        score += 40

    if website:
        score += 30

    return score