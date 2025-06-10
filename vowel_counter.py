# Vowel Counter Program

word = input("Enter a single word: ")
vowel_count = 0
vowels = "aeiouAEIOU"

for char in word:
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)
