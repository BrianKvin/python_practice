# Day 10 - Loops
# Iterate 0 to 10 using for loop, do the same using while loop.
for num in range(1, 11):
  print(num)

num = 1
while num <= 10:
  print(num)
  num += 1

# Iterate 10 to 0 using for loop, do the same using while loop.
for num in range(10, -1, -1):
  print(num)

num = 10
while num >= 0:
  print(num)
  num -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
"""
  #
  ##
  ###
  ####
  #####
  ######
  #######
"""
triangle = ""
for i in range(1, 8):
    triangle += "#" * i + "\n"
print(triangle)

# Use nested loops to create the following:
"""
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""

for row in range(8):
  for col in range(8):
    print('#', end=" ")
  print()

# Print the following pattern:

"""
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""
for i in range(11):
  print(f"{i} x {i} = {i * i}")

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
sum = 0
for num in range(101):
  sum += num
print("The sum of all numbers is", sum)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
sum_evens = 0
sum_odds = 0

for i in range(101):
  if i % 2 == 0:
      sum_evens += i
  else:
      sum_odds += i

print("The sum of all evens is", sum_evens)
print("The sum of all odds is", sum_odds)
