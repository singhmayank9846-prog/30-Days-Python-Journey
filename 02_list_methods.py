 # append()
number = [1,10,15,20,25,30,35]
number.append(40)
print(number) # ADD One number at the end of the List 

# extend()
number = [1,15,20]
number.extend([25,30,45])
print(number)   # ADD multiple limits to the end of the List

# insert()
number = [1,4,6,7,9,10]
number.insert(1,5)
print(number)   # Insert an element at a specific index

# remove
number = [1,3,5,6,8,3,10,15]
number.remove(3)
print(number)  # remove the first occurance value

# pop
number = [2,5,7,9,20]
number.pop()
print(number)  #removes and returns an element (default last)

# clear
number = [1,3,5,7,9,11]
number.clear()
print(number)  # clear all the value inside the list

# index
number = [5,7,9,11,13,15,17,23]
number.index(7)
print(number.index(7))   #With the help of index we find the position 

# Count
a = [1,2,4,5,4,6,4,8]
print(a.count(4))       # count help us to know how many times same number comes

#  sort()
a = [4,3,6,9,7,1]
a.sort()
print(a)       # It sort the list in place

# reverse
a = [1,4,7,8,10]
a.reverse()
print(a)

# len()
a = [1,3,5,6,7,8,9,13,24,46,57]
print(len(a))

"""Add → append, insert, extend

Remove → remove, pop, clear

Search → index, count

Arrange → sort, reverse"""