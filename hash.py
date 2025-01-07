# Import the regular expression library
import re

# Function to check the hash type
def identify_hash(hash_input):
    # Patterns for different hash types
    hash_patterns = {
        "MD5": r"^[a-fA-F0-9]{32}$",  # MD5 is 32 characters long
        "SHA1": r"^[a-fA-F0-9]{40}$", # SHA1 is 40 characters long
        "SHA256": r"^[a-fA-F0-9]{64}$" # SHA256 is 64 characters long
    }

    # List to store matching types
    possible_types = []

    # Check the input against each pattern
    for hash_type, pattern in hash_patterns.items():
        if re.match(pattern, hash_input):
            possible_types.append(hash_type)

    # Return the results
    if possible_types:
        return f"ithaa kuttaaa ninte hash: {', '.join(possible_types)}"
    else:
        return "matching aaya hash type onnum illa kuttaa veera nook."

# Ask the user for input
hash_input = input("Eeth hash aanu find cheyyandee: ")
result = identify_hash(hash_input)
print(result)
