# Original lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# Step 1: Join the two lists
front_end.extend(back_end)

# Step 2: Copy the joined list
full_stack = front_end.copy()

# Step 3: Insert 'Python' and 'SQL' after 'Redux' (which is at index 4)
# So we insert at index 5 and 6
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')

# Final output
print(full_stack)

# Exercise level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# sorted_ages = sorted(ages)
ages.sort()
print(ages)
# Find min and max age
min_age = min(ages)
max_age = max(ages)

print("Minimum age:", min_age)
print("Maximum age:", max_age)

# Add min and max to the list
ages.append(min_age)
ages.append(max_age)

print("Updated ages list:", ages)

sorted_ages = sorted(ages)
print(sorted_ages)

# Find the median age (one middle item or two middle items divided by two)
n = len(ages)
if n % 2 == 0:
  median = (ages[n//2] - 1 + ages[n//2] / 2)
else:
  median = ages[n//2]

print("Sorted ages:", ages)
print("Median age:", median)

# Find the average age (sum of all items divided by their number )
average_age = (sum(ages)) / n
print("Average age:", average_age)

# Find the range of the ages (max minus min)
range = max_age - min_age
print("range:", range)

# Compare the value of (min - average) and (max - average), use abs() method
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)

print("Average age:", average_age)
print("Min - Average (abs):", min_diff)
print("Max - Average (abs):", max_diff)

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries = ['Canada', 'Brazil', 'Germany', 'Kenya', 'India', 'Japan', 'Norway']

# Find the midpoint (first half gets the extra if odd)
mid_index = (len(countries) + 1) // 2

# Slice into two halves
first_half = countries[:mid_index]
second_half = countries[mid_index:]

print("First half:", first_half)
print("Second half:", second_half)

# Unpack the first three countries and the rest as scandic countries.
nations = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
China, Russia, USA, *scandic  = nations
print(scandic)