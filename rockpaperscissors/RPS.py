import random

def get_markov_chain_order(opponent_history, order):
    # Generate the Markov Chain transition matrix for a given order.
    chain = {}
    for i in range(len(opponent_history) - order):
        state = tuple(opponent_history[i:i+order])
        next_move = opponent_history[i+order]
        if state not in chain:
            chain[state] = {'R': 0, 'P': 0, 'S': 0}
        chain[state][next_move] += 1
    return chain

def predict_move(markov_chain, opponent_history, order):
    state = tuple(opponent_history[-order:])
    if state in markov_chain:
        return max(markov_chain[state], key=markov_chain[state].get)
    return random.choice(['R', 'P', 'S'])

def player(prev_play, opponent_history=[]):
    if not prev_play or not opponent_history:
        return random.choice(['R', 'P', 'S'])
    markov_chain = get_markov_chain_order(opponent_history, order=2)
    return predict_move(markov_chain, opponent_history, order=2)

# Define the bots for testing
def quincy(prev_play, opponent_history=[]):
    return "R"

def random_player(prev_play, opponent_history=[]):
    return random.choice(['R', 'P', 'S'])

def reflect_player(prev_play, opponent_history=[]):
    if not prev_play:
        return random.choice(['R', 'P', 'S'])
    return prev_play

def cycle_player(prev_play, opponent_history=[]):
    moves = ['R', 'P', 'S']
    if not opponent_history:
        return random.choice(moves)
    last_index = moves.index(opponent_history[-1])
    return moves[(last_index + 1) % len(moves)]

# The play function to run tests
def play(player1, player2, num_games, verbose=False):
    player1_wins = 0
    player2_wins = 0
    ties = 0

    for _ in range(num_games):
        p1_move = player1('', [])
        p2_move = player2('', [])
        if p1_move == p2_move:
            ties += 1
        elif (p1_move == 'R' and p2_move == 'S') or (p1_move == 'P' and p2_move == 'R') or (p1_move == 'S' and p2_move == 'P'):
            player1_wins += 1
        else:
            player2_wins += 1

        if verbose:
            print(f"Player 1: {p1_move}, Player 2: {p2_move}, Winner: {'Tie' if p1_move == p2_move else 'Player 1' if player1_wins > player2_wins else 'Player 2'}")

    return player1_wins, player2_wins, ties
