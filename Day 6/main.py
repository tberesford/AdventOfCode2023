import re


def part_one(timings, distancing):
    scores = []
    for index, time in enumerate(timings):
        score = 0
        i = 1

        while i < int(time):
            distance = (int(time) - i) * i
            if distance > int(distancing[index]):
                score += 1
            i += 1
        scores.append(score)
    return get_final_score(scores)


def get_values_over(timings, distancing):
    scores = []
    score = 0
    i = 0
    while i < timings:
        distance = (timings - i) * i
        if distance > distancing:
            score += 1
        i += 1
    scores.append(score)
    return get_final_score(scores)


def get_final_score(values):
    total_score = 0
    for val in values:
        if total_score == 0:
            total_score = val
        else:
            total_score *= val
    return total_score


if __name__ == '__main__':
    with open("data", "r") as f:
        data = f.read().split('\n')
    times = re.findall(r'\d+', data[0])
    distances = re.findall(r'\d+', data[1])

    scores = part_one(times.copy(), distances.copy())
    print(f'Part one answer: {scores}')
    times = int(''.join(times))
    distances = int(''.join(distances))
    scores = get_values_over(times, distances)
    print(f'Part two answer: {scores}')

