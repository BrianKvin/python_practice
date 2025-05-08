# Sets

# creating a new set
st = set()
st = {'item1', 'item2', 'item3', 'item4'}

# Getting set length
len(st)

#Accessing items in a set
print('item1' in st) 

# Adding one item to set
st.add('item5')
print('set:', st)

# Add multiple items to set
st.update(['item6', 'item7', 'item8', 'item9', 'item10'])
print('set:', st)

# Removing items from a set
st.remove('item10')
#remove a random item
#st.pop()
removed_item = st.pop()
removed_elem = st.remove()
print('set:', st)
print('removed item:', removed_item)
print('removed elem:', removed_elem)

# clear items in a set
st.clear()

#del set
del st

# converting a list to a set
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(list)

# joining sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

# Update This method inserts a set into a given set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)

# Finding Intersection Items
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2)

# Checking Subset and Super Set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

# Checking the Difference Between Two Sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2

# Finding Symmetric Difference Between Two Sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}

#Joining Sets
# If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False

