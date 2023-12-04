import re

with open("data", "r") as f:
    data = f.read().strip()
f.close()


def normalise(data):
    row = data.split('\n')
    numbers = [re.findall(r'\d', x) for x in row]
    return sum([int(n[0] + n[-1]) for n in numbers])


print(normalise(data))

strings = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine"
}

for val in strings:
    data = data.replace(val, strings[val])
print(normalise(data))
