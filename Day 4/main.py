import re


def get_numbers(row):
    to_check, win_card = row.split('|')
    to_check_numbers = re.findall(r'\d+', to_check)
    win_card_numbers = re.findall(r'\d+', win_card)
    winning_numbers = [int(number) for number in win_card_numbers if number in to_check_numbers]
    return len(winning_numbers)


def perform_games(card, total):
    points = 0
    amount_of_numbers = get_numbers(card)
    if amount_of_numbers > 0:
        points = 2 ** (amount_of_numbers-1)
    total += points
    return total, amount_of_numbers, points


if __name__ == '__main__':
    with open("data", "r") as f:
        data = f.read().strip()
    cards = [row.split(":")[1] for row in data.split('\n')]
    card_id = [[row.split(":")[0].replace(' ', ''), 1, 0] for row in data.split('\n')]  # [ Card_Game, number of copies,
    sum_points = 0                                                                        # number of points won in one
    for index, card in enumerate(cards):                                                  # game ]
        sum_points, amount_of_games_won, card_points = perform_games(card, sum_points)
        card_id[index][2] = card_points
        for n in range(index+1, index+(amount_of_games_won+1)):
            card_id[n][1] += card_id[index][1]
    part_two_sum = sum([card[1] for card in card_id])

    print(f"Part one answer: {sum_points}")
    print(f"Part two answer: {part_two_sum}")
