import numpy as np


def add_duplicates(input, length, distance):
    if np.count_nonzero(input == ".") == length:
        return distance
    else:
        return 1


def calculate_distance(end_value, expansion):
    distance = 0
    for val_one in range(1, hashtag):
        for val_two in range(val_one + 1, hashtag + 1):
            x_one, y_one = np.where(data == str(val_one))
            x_two, y_two = np.where(data == str(val_two))
            result = 0

            if x_one[0] < x_two[0]:
                for row in range(x_one[0], x_two[0]):
                    result += add_duplicates(data[row, :], data[row, :].shape[1], expansion)
            else:
                for row in range(x_two[0], x_one[0]):
                    result += add_duplicates(data[row, :], data[row, :].shape[1], expansion)
            if y_one[0] < y_two[0]:
                for col in range(y_one[0], y_two[0]):
                    result += add_duplicates(data[:, col], data[:, col].shape[0], expansion)
            else:
                for col in range(y_two[0], y_one[0]):
                    result += add_duplicates(data[:, col], data[:, col].shape[0], expansion)
            distance += result
    return distance


if __name__ == "__main__":
    with open("data", "r") as f:
        data = [list(line.strip('\n')) for line in f.readlines()]

    data = np.matrix(data)
    data = data.astype('U7')
    x, y = data.shape

    count, row, hashtag = 0, 0, 1
    while row < x:
        for char in range(len(data[:, row])):
            if data[row, char] == '#':
                data[row, char] = hashtag
                hashtag += 1
        row += 1

    hashtag -= 1
    part_one = calculate_distance(hashtag, 2)
    print(f"Part one answer is: {part_one}")
    part_two = calculate_distance(hashtag, 1000000)
    print(f"Part two answer is: {part_two}")
