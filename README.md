# elo
Calculate Elo ratings for players given match data.

## Usage
Calculate a new rating given prior information:

    import elo
    new = elo.new_rating(rating_a, rating_b, num_matches_a, score)