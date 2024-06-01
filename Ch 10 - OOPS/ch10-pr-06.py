# Change the self parameter inside the class to 'prag' and see the effects.

class Sample:
    def __init__(prag, name): # self is a normal parameter and it can be changed into any name
        prag.name = name

ob = Sample("Prag")
print(ob.name)