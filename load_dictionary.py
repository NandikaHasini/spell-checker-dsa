def load_dictionary():
    dictionary = set()

    with open("dictionary.txt", "r") as file:
        for word in file:
            dictionary.add(word.strip().lower())

    return dictionary
