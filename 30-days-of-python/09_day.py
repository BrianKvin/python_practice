# Exercise 1
'''
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
'''
age = int(input('Enter your age: '))
if age >= 18:
  print('You are old enough to learn to drive')
elif age < 18:
  print(f'You need {18 - age} more years to learn to drive')


'''
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
'''
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()

if new_fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(new_fruit)
    print("Updated fruit list:", fruits)


'''
Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
'''
month = input('Enter the month: ').capitalize()
if month in ['September', 'October', 'November']:
   print('The season is Autumn')
elif month in ['December', 'January', 'February,']:
   print('The season is Winter')
elif month in ['March', 'April', 'May']:
   print('The season is Spring')
elif month in ['June', 'July', 'August']:
   print('The season is Summer')
else:
   print('Invalid month')

'''
Here we have a person dictionary. Feel free to modify it!
'''
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
   skills = person['skills']
   middle_index = len(skills) // 2
   print('middle_skill: ', skills[middle_index])

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill:", has_python)

# 3. Check developer type based on skill combinations
if 'skills' in person:
    skills_set = set(person['skills'])

    if skills_set == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print("He is a backend developer")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# 4. Check marital status and country
if person.get('is_marred') and person.get('country') == 'Finland':
    full_name = f"{person['first_name']} {person['last_name']}"
    country = person['country']
    print(f"{full_name} lives in {country}. He is married.")