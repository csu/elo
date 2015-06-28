BASE_RATING = 1500

# greater than elo threshold: k-factor
K_FACTORS = {
    0: 32,
    (BASE_RATING*1.4): 24,
    (BASE_RATING*1.6): 1.6
}