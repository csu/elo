import constants
import math

def get_k_factor(player_rating, player_num_matches):
    if constants.K_FACTOR_MATCHES_THRESHOLD:
        if player_num_matches < constants.K_FACTOR_MATCHES_THRESHOLD:
            return constants.K_FACTOR_MATCHES_VALUE
    for i, thres in enumerate(constants.K_FACTOR_THRESHOLDS):
        if player_rating < thres:
            return constants.K_FACTORS[i]
    return constants.K_FACTORS[-1]

def expected_score(rating_a, rating_b):
    return 1/float(1+math.pow(10, (rating_b-rating_a)/float(400)))

def updated_rating(original_rating, k_factor, expected, actual):
    return original_rating+k_factor*(actual-expected)

def new_rating(rating_a, rating_b, num_matches_a, score):
    k_factor = get_k_factor(rating_a, num_matches_a)
    expected = expected_score(rating_a, rating_b)
    return updated_rating(rating_a, k_factor, expected, score)

def new_rating_funcs(rating_function, num_matches_function, player_a, player_b, score):
    rating_a = rating_function(player_a)
    rating_b = rating_function(player_b)
    num_matches_a = num_matches_function(player_a)
    return new_rating(rating_a, rating_b, num_matches_a, score)