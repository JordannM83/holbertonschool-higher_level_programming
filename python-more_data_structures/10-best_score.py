#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = None
    winner = None
    if not a_dictionary:
        return None
    for name, score in a_dictionary.items():
        if max_score is None:
            max_score = score
            winner = name
        if score > max_score:
            max_score = score
            winner = name
    return winner
