# # Learning Datatypes In Python
# # 7 Types Of Datatypes

# # TEXT TYPE
# # 1 String str

customer_name = "Mayank"
print("customer name is :",customer_name)
print("customer datatype is :",type(customer_name))

# # NUMERIC TYPES
# # 2.1 Int

rating = 5
order_quantity = 35
print("customer datatype :",type(rating))
print("customer data_type :",type(order_quantity))

# # 2.2 Float DECIMAL NUMBER
order_amount = 3850.68
print("customer data_type is :",type(order_amount))

# # 2.3 Complex NUMBER + IMAGINARY VALUE(j)
a = 6 + 5j
print("customer data_type is :",type(a))

# # 3 BOOLEAN TYPE bool (TRUE/FALSE)
Is_type = True
print("customer data_type is :",type(Is_type))

# # 4 SEQUENCE TYPE 
#  # 4.1 List
cities = ["Mumbai","Delhi","Kolkata","Katihar","Hydrabad"]
print(cities)
print(type(cities))

# # 4.2 Tuple 
dimensions = (1920,1860,2026)
print(dimensions)
print(type(dimensions))

# # 4.3 Range 
number = range(1,11)
print(list(number))
print(type(number))

# # 5 Dictonary Dict
Students = {
    "name" : "Mayank singh",
    "class" : "A",
    "Roll_No" : 9846
}
print(Students)
print(type(Students)
      )

#  #  6  set 
number = {1,2,2,3,3,4,4,4,4,5,5,5,}
print(number)
print(type(number))

# # 7 None Tpe
Remarks = None
print(Remarks,type(Remarks))
 

