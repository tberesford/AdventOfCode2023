
def get_difference(numbers):
    total_differences = []
    while True:
        differences = []
        for i in range(0, len(numbers)-1):
            differences.append(int(numbers[i+1]) - int(numbers[i]))
        total_differences.append(differences)

        if differences.count(differences[0]) == len(differences):
            break
        else:
            numbers = differences

    if len(total_differences) == 1:
        difference = total_differences[0][0]
    else:
        difference = 0
        for row in reversed(total_differences):
            difference += row[-1]
    return difference


def go_backwards(numbers):
    total_differences = []
    while True:
        differences = []
        for i in range(0, len(numbers) - 1):
            differences.append(int(numbers[i + 1]) - int(numbers[i]))
        total_differences.append(differences)
        if differences.count(differences[0]) == len(differences):
            break
        else:
            numbers = differences

    if len(total_differences) == 1:
        difference = total_differences[0][0]
    else:
        difference = total_differences[-1][0]
        total_differences[-1].insert(0, difference)
        for row in reversed(total_differences[:-1]):
            row.insert(0, row[0] - difference)
            difference = row[0]
    return difference


if __name__ == "__main__":
    with open("data", "r") as f:
        data = f.read().split('\n')

    for i, row in enumerate(data):
        data[i] = row.split(' ')

    tally_of_differences = 0
    for row in data:
        diff = get_difference(row)
        tally_of_differences += int(row[-1]) + diff

    print(f"Part one answer: {tally_of_differences}")

    tally_of_differences = 0
    for row in data:
        diff = go_backwards(row)
        tally_of_differences += int(row[0]) - diff

    print(f"Part two answer: {tally_of_differences}")
