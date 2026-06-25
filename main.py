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



print("\n10 sided die") 

ten_sided = Die(10)
for i in range(10):
    ten_sided.roll_die()


print("\n20 sided die")

twenty_sided = Die(20)
for i in range(10):
    twenty_sided.roll_die()