import re

result = re.search(r'(\d+) ([-+*/]) (\d+)', '10 + 5')

print(result.groups())

print(result.group(1))

print(result.group(2))

print(result.group(3))