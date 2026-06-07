import re

street = r'\d+ [A-Z][a-z]* [A-Z][a-z]*'

print('Match' if re.fullmatch(street, '123 Main Street') else 'No match')

print('Match' if re.fullmatch(street, 'Main Street') else 'No match')