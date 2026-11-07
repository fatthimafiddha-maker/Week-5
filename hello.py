# print("Hello, World!")
# print("My name is a Python learner.")
# print("I am starting my journey from zero to hero!")

import copy
a = [[1,2],[3,4]]

# b= copy.copy(a)

# b[0][0]=20
# print("original",a)
# print("copied",b)

c=copy.deepcopy(a)
c[0][0]=300
print("original.deep",a)
print("copied.deep",c)
