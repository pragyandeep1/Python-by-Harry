# Create a class with class attribute a; create an object from it; set directly obj.a=0. Does it change the class attribute?

class Sample:
    a = "Prag" # class attribute

ob = Sample()
ob.a = "Vickings" # instance attribute
# Sample.a = "Henry" modify the class attribute

print(Sample.a)
print(ob.a)