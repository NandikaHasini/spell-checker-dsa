from edit_distance import edit_distance

def get_suggestions(word, dictionary):
    suggestions = []

    for dict_word in dictionary:
        if abs(len(dict_word) - len(word)) <= 2:
            dist = edit_distance(word, dict_word)
            if dist <= 2:
                suggestions.append((dist, dict_word))

    suggestions.sort()
    return [word for _, word in suggestions[:5]]
