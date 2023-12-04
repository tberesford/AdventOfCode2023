import re


# part one
def counter(row):
    items = row.split(';')
    for item in items:
        for colour in item.split(','):
            number = re.findall(r'\d+', colour)
            for colour_key in colours:
                if colour_key in colour and int(number[0]) > colours[colour_key]:
                    return False
    return True


# part two
def maximise(row, colour_values):
    items = row.split(';')
    for item in items:
        for colour in item.split(','):
            number = re.findall(r'\d+', colour)
            for colour_key in colour_values:
                if colour_key in colour:
                    colour_values[colour_key] = max(colour_values[colour_key], int(number[0]))
    return colour_values['green'] * colour_values['blue'] * colour_values['red']


if __name__ == "__main__":
    with open("data", "r") as f:
        data = f.read().strip()
    data = [x.split(':')[1] for x in data.split('\n')]

    total_id, total_sum = 0, 0
    for i, x in enumerate(data):
        colours = {'red': 12, 'green': 13, 'blue': 14}
        part_one_ans = counter(x)
        if part_one_ans:
            total_id = total_id + (i+1)

        colours = {'red': 0, 'green': 0, 'blue': 0}
        part_two_ans = maximise(x, colours)
        total_sum += part_two_ans

    print(f"Answer to part one is: {total_id}")
    print(f"Answer to part two is: {total_sum}")
