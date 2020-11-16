# In this notebook, you will simulate a system with of three nuclei  AA ,  BB  and  CC  where  AA  decays into  BB  and  BB  decays into  CC . If exposed to a neutron flux nucleus  CC  can be activated into a nucleus  AA .

import numpy
from matplotlib import pyplot as plt
import random

# Implement a function that tells whether a transition has occured,
# based on the transition probability and a random number. Use the random number r from random.random()
# and use the procedure described in the notes so that the checks can work in a reproducible way.

def has_transitioned(p):
    r = random.random()
    return True if p>r else False

random.seed(9867)
assert [ has_transitioned(0.5) for i in range(10)] == [False, False, True, False, False, False, False, True, False, True]

def evolveOne(currentState, rules):
    # YOUR CODE HERE
    for r in rules:
        if currentState  == r[0]:
            return r[1] if has_transitioned(r[2]) else r[0]
        else:
            continue
    else:
        return currentState


# these tests are worth 1 mark
alwaysDecayRules = [
    ('A', 'B', 1.0),
    ('B', 'C', 1.0)
]
assert evolveOne('A', alwaysDecayRules) == 'B'
assert evolveOne('B', alwaysDecayRules) == 'C'

# these tests are worth 2 mark
random.seed(112211)
testRules = [
    ('A', 'B', 0.33),
    ('B', 'C', 0.75)
]
assert evolveOne('A', testRules) == 'A'
assert evolveOne('A', testRules) == 'A'
assert evolveOne('A', testRules) == 'A'
assert evolveOne('A', testRules) == 'A'
assert evolveOne('A', testRules) == 'B'

assert evolveOne('B', testRules) == 'B'
assert evolveOne('B', testRules) == 'C'
assert evolveOne('B', testRules) == 'C'
assert evolveOne('B', testRules) == 'C'
assert evolveOne('B', testRules) == 'C'

# with no rules there should be no change
assert evolveOne('C', testRules) == 'C'

# Now implement a function that takes a list of states and transition them according to the rules passed as argument.
# This function should return a new vector of states, it should not modify the state passed as an argument!


def evolveMany(states, rules):
    newState = []
    # YOUR CODE HERE
    for s in states:
        newState.append(evolveOne(s,rules))
    return newState

# these tests are worth 1 mark
random.seed(112287)
testRules = [
    ('A', 'B', 0.33),
    ('B', 'C', 0.75)
]
initialTestArray = ['A','B','C']*5
evolvedTest = evolveMany(initialTestArray, testRules)
targetArray = ['B', 'C', 'C', 'A', 'C', 'C', 'A', 'B', 'C', 'A', 'C', 'C', 'B', 'C', 'C']
assert evolvedTest == targetArray
# checks the initial array is left unchanged
assert initialTestArray == ['A','B','C']*5

# Define a function that evolves a system that starts with initial amounts NA, NB and NC of  AA ,
# BB  and  CC  nuclei and evolved it in n_timestep from time  t=0t=0  to  t=tmaxt=tmax .
# The function should return three arrays, one for each atom type, of the number of nuclei
# of that type at each time step. Each array should contain n_timestep+1 elements including the initial amount.

def evolve_system(NA, NB, NC, rules, n_step):
    state = (['A'] * NA)+(['B'] * NB)+(['C'] * NC)

    A_count = numpy.empty(n_step + 1, dtype=int)
    B_count = numpy.empty(n_step + 1, dtype=int)
    C_count = numpy.empty(n_step + 1, dtype=int)

    # YOUR CODE HERE
    A_count[0] = NA
    B_count[0] = NB
    C_count[0] = NC
    for i in range(n_step):
        state = evolveMany(state, rules)
        A_count[i+1] = state.count('A')
        B_count[i+1] = state.count('B')
        C_count[i+1] = state.count('C')
    return A_count, B_count, C_count


# these tests are worth 2 marks
rules = [
    ('A', 'B', 0.0033),
    ('B', 'C', 0.0075),
    ('C', 'A', 0.009)

]

r1, r2, r3 = evolve_system(0, 0, 250, rules, 17)
assert len(r1) == 18
assert len(r2) == 18
assert len(r3) == 18

# these tests are worth 2 marks
testrules = [
    ('A', 'B', 0.086),
    ('B', 'C', 0.075),
    ('C', 'A', 0.19)

]

random.seed(9485)
r1, r2, r3 = evolve_system(200, 200, 200, testrules, 20)
print(r1)
print(r2)
print(r3)
assert (r1 == [200, 213, 233, 250, 258, 251, 266, 263, 259, 260, 265, 259, 256,
               255, 258, 256, 259, 253, 249, 247, 253]).all()
assert (r2 == [200, 198, 201, 206, 205, 214, 214, 212, 216, 221, 225, 234, 236,
               238, 234, 235, 231, 245, 253, 256, 252]).all()
assert (r3 == [200, 189, 166, 144, 137, 135, 120, 125, 125, 119, 110, 107, 108,
               107, 108, 109, 110, 102, 98, 97, 95]).all()

