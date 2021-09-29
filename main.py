# Programmer: Aiden Sterling
# Date: 9/28/21
# Description: Making an input function that takes the amount of people and tables, then distributes them as evenly as possible.

from math import*

# Input
people = int(input("How many people are there? "))
tables = int(input("How many tables are there? "))
print()

# Math
division = int(people // tables)
left_over = int(people % tables)
odd_people = int(division + 1)
odd_tables = int(left_over % tables)
norm_tables = int(tables - odd_tables)

# Output
print(f"{norm_tables:,.0f} tables will have {division:,.0f} people.")
print(f"{odd_tables:,.0f} tables will have {odd_people:,.0f} people.")