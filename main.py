"""
Name: Chris Martinez
Assignment: Participation Activity 3
File Purpose: Creates a 6, 10, and 20 and rolls each one 10 times
Date: June 25, 2026
"""

from die import Die

print("6 sided die")

six_sided = Die()
for i in range(10):
    six_sided.roll_die()