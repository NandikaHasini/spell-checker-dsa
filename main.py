from load_dictionary import load_dictionary
from checker import is_correct
from suggestions import get_suggestions

def spell_check_sentence(sentence):
    dictionary = load_dictionary()
    print("Words loaded:", len(dictionary))
    words = sentence.lower().split()

    for word in words:
        if is_correct(word, dictionary):
            print(f"✔ '{word}' is correct")
        else:
            print(f"❌ '{word}' is incorrect")
            print("   Suggestions:", get_suggestions(word, dictionary))

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    spell_check_sentence(sentence)
