import itertools, re

# Define the substitution keys
keys = [
    "T=A,E,J,T,X",  # Key for 'T'
    "I=B,G,I,F,W",  # Key for 'I'
    "Y=C,D,N,U,Y",  # Key for 'Y'
    "L=F,L,O,Q,V",  # Key for 'L'
    "R=R",          # Key for 'R'
    "H=H,K,M,S"     # Key for 'H'
]

# Create a dictionary to map each character to its possible substitutions
sub_dict = {}
for key in keys:
    char, subs = key.split('=')
    sub_dict[char] = subs.split(',')

# Function to generate all possible combinations for a single word
def generate_combinations(word, sub_dict):
    possible_subs = [sub_dict[char.upper()] for char in word if char.upper() in sub_dict]
    all_combinations = list(itertools.product(*possible_subs))
    return [''.join(comb).lower() for comb in all_combinations]  # Make sure all are lowercase

# Dictionary steps
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return [word.lower().strip() for word in words]

# Load the dictionary
dictionary = load_dictionary('./words.txt')

# Function to handle multiple words and collect all matches
def decode_string(input_string, sub_dict, dictionary):
    words = input_string.split()  # Split the input string into individual words
    all_matches = []  # This will store the list of matches for each word

    for word in words:
        possible_words = generate_combinations(word, sub_dict)
        matches = []
        for example in possible_words:
            if example in dictionary:
                print(f"Match found for '{word}': {example}")
                matches.append(example)
        
        # Append the matches for this word (or note if no match found)
        if matches:
            all_matches.append(matches)
        else:
            all_matches.append([f"[No match for '{word}']"])

    return all_matches

# Input string to decode
input_string = input("Enter encoded string: ")

# Decode the input string and collect all matches
decoded_matches = decode_string(input_string, sub_dict, dictionary)

# Print all matches
for i, matches in enumerate(decoded_matches):
    print(f"Matches for word {i+1}: {matches}")
