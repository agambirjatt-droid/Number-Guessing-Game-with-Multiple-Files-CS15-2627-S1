def update_score(current_score):
    new_score = current_score - 10
    # you lose 10 points for every wrong guess.
    if new_score < 0:
        # you go back to 0 as your score.
        return 0
    return new_score
def get_rating(score):
    if score >= 80:
        return "excellent"
    elif score >= 50:
        return "good"
    else:
        return "Keep practicing bro"





