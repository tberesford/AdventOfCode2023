
characters = ["$", "%", "&", "*", "-", "=", "+", "/", "@", "#"]
gears = "*"


def check_gears(rows, head, tail):
    for row in rows:
        if gears in row[head:tail]:
            return row[head:tail].index(gears), row
    return False, False


def check_rows(rows, head, tail):
    for row in rows:
        for char in characters:
            if char in row[head:tail]:
                return True
    return False


def locate_number_in_row(row, head):
    index = head
    while index < len(row) and x[index].isdigit():
        index += 1
    tail = index
    number = int(row[head:tail])
    head -= 1
    tail += 1
    tail = len(x) if tail > len(x) else tail
    head = 0 if head < 0 else head
    return head, tail, number


def get_rows(y, data):
    if y == 0:
        rows = [data[0], data[1]]
    elif 0 < y < (len(x) - 1):
        rows = [data[y - 1], data[y], data[y + 1]]
    else:
        rows = [data[y - 1], data[y]]
    return rows


def part_one(x, data, value):
    i = 0
    while i < len(x):
        number = ''
        head, tail = 0, 0
        if x[i].isdigit():
            head, tail, number = locate_number_in_row(x, i)
            i = tail - 1
        i += 1

        rows = get_rows(y, data)
        ans = check_rows(rows, head, tail)
        if ans:
            value += number
    return value


def part_two(x, data, y, gear_dictionary):
    i = 0
    while i < len(x):
        number = ''
        head, tail = 0, 0
        if x[i].isdigit():
            head, tail, number = locate_number_in_row(x, i)
            i = tail - 1

        rows = get_rows(y, data)
        ans, row = check_gears(rows, head, tail)
        if row:
            gear_height = data.index(row)
            gear_index = head+ans
            add_to_dict = True
            for item in gear_dictionary:
                if len(item) > 1 and [gear_height, gear_index] == item[0]:
                    gear_dictionary.append([int(item[1]) * int(number)])
                    gear_dictionary.remove(item)
                    add_to_dict = False
                    break
            if add_to_dict:
                gear_dictionary.append([[gear_height, gear_index], number])
        i += 1
    return gear_dictionary


if __name__ == '__main__':
    with open("data", "r") as f:
        data = f.readlines()

    data = [row.replace('\n', '') for row in data]
    part_one_sum = 0
    new_tally = []

    for y, x in enumerate(data):
        part_one_sum = part_one(x, data, part_one_sum)
        new_tally = part_two(x, data, y, new_tally)

    part_two_sum = sum([numbers[0] for numbers in new_tally if len(numbers) == 1])

    print(f"Part one answer: {part_one_sum}")
    print(f"Part two answer: {part_two_sum}")
