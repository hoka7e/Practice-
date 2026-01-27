# Booleans represent one of two values: True or False.
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) # False

a = 200
b = 33

if b > a: #True -> "b is greater than a" will be primted
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello")) #True , Any string is True, except empty strings.
print(bool(15)) #True , Any number is True, except 0.

#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

