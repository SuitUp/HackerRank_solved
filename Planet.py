"""
Suppose I want to flatten a given 2-D list and only include those strings whose lengths are less than 6:
planets = [[‘Mercury’, ‘Venus’, ‘Earth’], [‘Mars’, ‘Jupiter’, ‘Saturn’], [‘Uranus’, ‘Neptune’, ‘Pluto’]]
Expected Output: flatten_planets = [‘Venus’, ‘Earth’, ‘Mars’, ‘Pluto’]
"""
# 2-D list of planets. Solve using Nested List approach.
planets = [['Mercury', 'Venus', 'Earth'], 
            ['Mars', 'Jupiter', 'Saturn'], 
            ['Uranus', 'Neptune', 'Pluto']]

#E_list = [] # empty list.

print([planet for sublist in planets for planet in sublist if len(planet) < 6])
