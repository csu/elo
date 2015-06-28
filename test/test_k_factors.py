from elo.constants import *
from elo.elo import get_k_factor

TEST_RATINGS = [0, BASE_RATING] + K_FACTOR_THRESHOLDS
MATCH_NUMS = [
    0, 
    K_FACTOR_MATCHES_THRESHOLD-1, 
    K_FACTOR_MATCHES_THRESHOLD, 
    K_FACTOR_MATCHES_THRESHOLD+1
]

class TestKFactors():
    def test_under_matches_threshold(self):
        for rating in TEST_RATINGS:
            assert get_k_factor(rating, K_FACTOR_MATCHES_THRESHOLD-1) == K_FACTOR_MATCHES_VALUE

    def test_thresholds(self):
        for matches in MATCH_NUMS:
            if matches > K_FACTOR_MATCHES_THRESHOLD:
                for i in range(len(K_FACTOR_THRESHOLDS)):
                    assert get_k_factor(K_FACTOR_THRESHOLDS[i]-1, matches) == K_FACTORS[i]
                    assert get_k_factor(K_FACTOR_THRESHOLDS[i]+1, matches) == K_FACTORS[i+1]