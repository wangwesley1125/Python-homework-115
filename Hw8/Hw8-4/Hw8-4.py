'''
(Character Frequency Analysis) In cryptoanalysis, the technique of character frequency analysis is often used to decipher a message when the key is unknown. This technique calculates the frequency of each character in the encrypted text and maps this to the
frequency of characters used in, for instance, the English language. Write a script that uses
a dictionary to summarize the frequency of each letter in a given text. Ignore case, ignore
spaces and assume that the user does not enter any punctuation. Display a two-column
table of the letters and their frequency.
'''

passwords = "ThisisapasswordforPython"

password_count = {}

for password in passwords:
    if password.lower() in password_count:
        password_count[password.lower()] += 1
    else:
        password_count[password.lower()] = 1

print(f"{"Letter": <7} Frequency")

for password, count in sorted(password_count.items()):
    print(f"{password: <7} {count}")