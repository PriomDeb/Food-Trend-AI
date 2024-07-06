def calculate_positive_score(ratings):
    positive_ratings = ratings[ratings >= 3]
    score = (len(positive_ratings) / len(ratings)) * 100 if len(ratings) > 0 else 0
    return score

def calculate_negative_percentage(ratings):
    positive_ratings = ratings[ratings < 3]
    score = (len(positive_ratings) / len(ratings)) * 100 if len(ratings) > 0 else 0
    return score

def calculate_neutral_percentage(ratings):
    positive_ratings = ratings[ratings == 3]
    score = (len(positive_ratings) / len(ratings)) * 100 if len(ratings) > 0 else 0
    return score

def calculate_positive_percentage(ratings):
    positive_ratings = ratings[ratings >= 4]
    score = (len(positive_ratings) / len(ratings)) * 100 if len(ratings) > 0 else 0
    return score

def score(score):
  return f"{score:.2f}%"


