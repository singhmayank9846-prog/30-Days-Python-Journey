# 1️⃣ count()
t = (1,3,6,7,3,9,3,10)
print(type(t))     #Tuple
print(t.count(3))  #It gives the result how many times a number comes in Tuple

# 2️⃣ index()
t = (10,20,30,40)
print(t.index(30))   #Returnds the element of the irst occurance of the element

# 3️⃣ len()
t = (1,3,5,7,9)
print(len(t))  # Returns the number of elements

# 4️⃣ min() / max()
t =(3,5,8,9)
print(min(t))   #Returns the minimum value
print(max(t))   #Returns the maximum value

# 5️⃣ sum()
t = (2,4,6,5,7,8,9,10)
print(sum(t))  #Returns the total sum of all numeric elements

# 6️⃣ Membership (in)

t = (2,34,45,67,78,956,746,74,76,77,67,567,57)
print(34 in t)   #It checks weather the element is present in the tuple or not
print(3939 in t) #It checks weather the element is present in the tuple or not

# 7️⃣ Indexing & Slicing

t = (23,45,67,14,687,789,1234,45678,345456)
print(t[3])     #Indexing
print(t[3:5])   #Slicing

