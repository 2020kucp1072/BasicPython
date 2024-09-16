def check_vowel_consonant(ch):
    """
    Checks whether a character is a vowel or consonant.
    
    Parameters:
    ch (str): The character to check.
    
    Returns:
    str: "Vowel" or "Consonant".
    """
    vowels = 'AEIOUaeiou'
    if ch in vowels:
        return "Vowel"
    else:
        return "Consonant"

# Main
ch = input("Enter an alphabet: ")
if ch.isalpha() and len(ch) == 1:
    print(f"{ch} is a {check_vowel_consonant(ch)}.")
else:
    print("Please enter a single alphabet.")
