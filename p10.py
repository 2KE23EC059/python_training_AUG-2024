#Program to check if the alphabet is Vowel or Consonant
def check_vowel_or_consonant(char):
    char = char.lower()

    if char in ('a', 'e', 'i', 'o', 'u'):
        return f"{char} is a vowel."
    else:
        return f"{char} is a consonant."
user_input = input("Enter an alphabet: ")
if len(user_input) == 1 and user_input.isalpha():
    result = check_vowel_or_consonant(user_input)
    print(result)
else:
    print("Please enter a valid single alphabet.")
