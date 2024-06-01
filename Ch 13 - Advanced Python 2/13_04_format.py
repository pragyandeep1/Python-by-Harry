name = "Prag"
channel = "CodingWagonPrag"
type = "counselling"
# a = f"This is {name}"
# a = "This is {}".format(name)
# a  = "This is {} and his date is {}".format(name, channel)
a  = "This is {1} and his {2} date is {0}".format(name, channel, type)
b  = "This is {} and his {} date is {}".format(name, channel, type)
c = "{} is a good {}".format("Prag", "Man")
# c = "{1} is a good {0}".format("Prag", "Man")
print(a)
print(b)
print(c)
