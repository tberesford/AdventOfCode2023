import math


def make_move(node, direction):
    return node[0] if direction == 'L' else node[1]


if "__main__" == __name__:
    with open("data", "r") as f:
        data = f.read().split('\n')
    data.remove('')
    moves = list(data[0])
    nodes = {}
    for item in data[1:]:
        head, tail = item.split(' = ')
        tail = tail.strip('(').strip(')')
        nodes[head] = list(tail.split(', '))

    total_amount = []
    print(f'There are: {len(moves)} moves to make.')
    print('Beginning...')
    amount_of_moves = 0
    for node in nodes:
        if node[-1] == 'A':
            head = node
            amount_of_moves = 0
            while True:
                head = make_move(nodes[head], moves[amount_of_moves % len(moves)])
                amount_of_moves += 1
                if head[-1] == 'Z':
                    break
            total_amount.append(amount_of_moves)

    print(f"Part one answer is: {amount_of_moves}")  # Not correct as modified for part two
    print(f"Part two answer is: {math.lcm(*total_amount)}")
