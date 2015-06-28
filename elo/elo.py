import constants

def get_k_factor(player_rating, player_num_matches):
    if constants.K_FACTOR_MATCHES_THRESHOLD:
        if player_num_matches < constants.K_FACTOR_MATCHES_THRESHOLD:
            return constants.K_FACTOR_MATCHES_VALUE
    for i, thres in enumerate(constants.K_FACTOR_THRESHOLDS):
        if player_rating < thres:
            return constants.K_FACTORS[i]
    return constants.K_FACTORS[-1]