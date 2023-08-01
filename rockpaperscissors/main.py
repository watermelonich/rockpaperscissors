from RPS import player, quincy, random_player, reflect_player, cycle_player, play

# Test against Quincy bot
print("Testing against Quincy bot:")
play(player, quincy, num_games=1000, verbose=True)

# Test against Random bot
print("\nTesting against Random bot:")
play(player, random_player, num_games=1000, verbose=True)

# Test against Reflect bot
print("\nTesting against Reflect bot:")
play(player, reflect_player, num_games=1000, verbose=True)

# Test against Cycle bot
print("\nTesting against Cycle bot:")
play(player, cycle_player, num_games=1000, verbose=True)
