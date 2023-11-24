from graph import *
from collections import deque
import random

def exo_1():
    # Create an instance of the Graph class
    graph = Graph()

    # Add vertices to the graph
    for i in range(1, 13):
        sommet = Sommet(i)
        graph.addSommet(sommet)

    # Add arcs to represent the "divisor of" relationship
    for i in range(1, 13):
        for j in range(1, 13):
            if j % i == 0:
                sommet1 = graph.getSommet(i)
                sommet2 = graph.getSommet(j)
                graph.addArc(sommet1, sommet2)

    # Print the graph
    print(graph)


def exo_2():
    # Define the initial state
    position = ['left', 'right']

    initial_state = {
        'goat': 'left',
        'cabbage': 'left',
        'wolf': 'left',
        'boat': 'left'
    }

    # Define the goal state
    goal_state = {
        'goat': 'right',
        'cabbage': 'right',
        'wolf': 'right',
        'boat': 'right'
    }

    # Define the valid actions
    invalid_actions = [{
        'goat': 'right',
        'cabbage': 'left',
        'wolf': 'right',
        'boat': 'left'
    }, {
        'goat': 'left',
        'cabbage': 'right',
        'wolf': 'left',
        'boat': 'right'
    }, {
        'goat': 'right',
        'cabbage': 'right',
        'wolf': 'left',
        'boat': 'left'
    }, {
        'goat': 'left',
        'cabbage': 'left',
        'wolf': 'right',
        'boat': 'right'
    }]
    
    tried_actions = []
    state = initial_state
    previous_state = state
    while state != goal_state:
        state, tried_actions = try_actions(state.copy(), tried_actions)
        print(state)
        if state in invalid_actions:
            state = previous_state

    return state

def try_actions(state, tried_actions):
    tmp_state = state
    while tmp_state in tried_actions:
        with_boat = who_are_with_boat(tmp_state)
        if tmp_state['boat'] == 'left':
            tmp_state['boat'] = 'right'
            # print(with_boat)
            rand = with_boat[random.randint(0,len(with_boat)-1)]
            # print(rand)
            tmp_state[rand] = 'right'
        else:
            tmp_state['boat'] = 'left'
            # tmp_state[with_boat[random.randint(0,len(with_boat)-1)]] = 'left'
            rand = with_boat[random.randint(0,len(with_boat)-1)]
            # print(with_boat)
            # print(rand)
            tmp_state[rand] = 'left'

        if tmp_state in tried_actions:
            tmp_state = state
    
    tried_actions.append(tmp_state.copy())
    return tmp_state, tried_actions

def who_are_with_boat(state):
    with_boat = []
    for key, value in state.items():
        if value == state['boat']:
            with_boat.append(key)
    return with_boat

print(exo_1())
