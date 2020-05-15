import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import random

player_one_a_prob = .5
player_one_b_prob = .5
player_two_a_prob = .25
player_two_b_prob = .25

def hit_cup(n, p):
    # Return True if a cup is hit and False otherwise
    chance_of_hitting = 1 - scipy.stats.binom.pmf(0, n, p)
    return random.random() < chance_of_hitting

def simulate_num_turns():
    team_one_cups = 10
    team_two_cups = 10
    team_one_turn = True
    num_turns = 0
    while team_one_cups > 0 or team_two_cups > 0:
        num_turns += 1
        # Single turn
        if team_one_turn:
            player_a_hit = hit_cup(team_one_cups, player_one_a_prob)
            player_b_hit = hit_cup(team_one_cups, player_one_b_prob)

            if not player_a_hit or not player_b_hit:
                team_one_turn = False
            team_one_cups = team_one_cups - int(player_a_hit) - int(player_b_hit)
        else:
            player_a_hit = hit_cup(team_two_cups, player_two_a_prob)
            player_b_hit = hit_cup(team_two_cups, player_two_b_prob)

            if not player_a_hit or not player_b_hit:
                team_one_turn = True
            team_two_cups = team_two_cups - int(player_a_hit) - int(player_b_hit)
    return num_turns

num_turns = []
for _ in range(10000):
    num_turns.append(simulate_num_turns())
    
plt.hist(num_turns)
plt.ylabel("count")
plt.xlabel("num minutes")
plt.title("10000 simulations of beer pong")
