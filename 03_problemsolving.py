# Check that  tuple type cannot be changed in Python.

a = (23,456,"Mayank",5677)
a[2] = "Singham"
print(a)    #'tuple' object does not support item assignment(Immutable)
