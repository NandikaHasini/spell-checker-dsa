# Dictionary-Based Spell Checker (DSA Project)
This project implements a **spell checker from scratch using core Data Structures and Algorithms (DSA)**.  
It validates words against a large English dictionary and suggests corrections for misspelled words using **Edit Distance (Dynamic Programming)**.
The focus of this project is **algorithmic problem-solving**, not third-party libraries or APIs.

## Problem Statement
Manual spell checking is inefficient and error-prone.  
A reliable spell checker must:
- Quickly verify whether a word exists
- Suggest the closest valid alternatives when errors occur
This project addresses the problem using **efficient data structures and string algorithms**.

## Technical Approach:

### Dictionary Storage
- Implemented using a **Hash Set**
- Enables constant-time word validation

### Spell Validation
- Each word is checked strictly against the dictionary
- Words not found are flagged as incorrect

### Suggestion Generation
- Candidate words are evaluated using **Edit Distance**
- Dynamic Programming is used to calculate the minimum number of operations required

### Ranking Strategy
- Suggestions are sorted by minimum edit distance
- Top matches are returned

## Algorithms & Data Structures Used
- Hash Set
- Dynamic Programming (Edit Distance)
- String manipulation algorithms
- Sorting algorithms
- 
## Key Features
- Offline, dictionary-based spell checking
- Fast word lookup
- Accurate correction suggestions
- Modular and readable code structure
- Zero external dependencies

## Project Structure

spell_checker/
├── dictionary.txt
├── load_dictionary.py
├── checker.py
├── edit_distance.py
├── suggestions.py
├── main.py
└── README.md

RUN:
python main.py

Sample Input:
that coupan is mine

Sample Output:

✔ 'that' is correct
❌ 'coupan' is incorrect
   Suggestions: ['coupon']
✔ 'is' is correct
✔ 'mine' is correct

Limitations:

    Checks only word validity, not grammar
    Does not handle contractions or slang
    Accuracy depends on dictionary coverage

Possible Improvements:

    Trie-based optimization
    Auto-correction feature
    Context-aware suggestions
    Support for multiple languages
