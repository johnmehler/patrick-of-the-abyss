# Define the substitution keys
keys = [
    "T=A,E,J,T,X",  # Key for 'T'
    "I=B,G,I,F,W",  # Key for 'I'
    "Y=C,D,N,U,Y",  # Key for 'Y'
    "L=F,L,O,Q,V",  # Key for 'L'
    "R=R",          # Key for 'R'
    "H=H,K,M,S"     # Key for 'H'
]

# Create a dictionary to map each letter from the right side of the key to the left
encode_dict = {}
for key in keys:
    left_value, right_values = key.split('=')
    right_list = right_values.split(',')
    for right_value in right_list:
        encode_dict[right_value] = left_value

# Function to encode the input
def encode_input(input_string, encode_dict):
    encoded_result = ""
    
    # For each character in the input, find the corresponding letter on the right side of the key
    for char in input_string.upper():  # Convert to uppercase for consistency
        if char in encode_dict:
            encoded_result += encode_dict[char].lower()  # Replace with the left-side value
        else:
            encoded_result += char.lower()  # Leave unchanged if not found in the key
    
    return encoded_result

# Take input from the user
user_input = input("Enter the string to encode: ")

# Encode the input
encoded_output = encode_input(user_input, encode_dict)

# Output the encoded response
print(f"Encoded response: {encoded_output}")
