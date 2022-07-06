def get_winner(ballots):
    candidates = {}
    for vote in ballots:
        if vote in candidates.keys():
            candidates[vote] += 1
        else:
            candidates[vote] = 1
    for key in candidates:
        if candidates[key] / sum(candidates.values()) > 0.5:
            return key
    return None


get_winner(("A"))
get_winner(("A", "A", "A", "B", "B", "B", "A"))
get_winner(("A", "A", "A", "B", "B", "B"))
get_winner(("A", "A", "A", "B", "C", "B"))
get_winner(("A", "A", "B", "B", "C"))
