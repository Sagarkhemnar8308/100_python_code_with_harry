class Employee:

    def __init__(self, name, sallary):
        self.name = name
        self.sallary = sallary
    
    @classmethod
    def fromString(cls, string):
        return cls(string.split('-')[0], string.split('-')[1])

    
e1 = Employee("sagar", "12000")
print(e1.name)
print(e1.sallary)

string = "john-1300"
e2 = Employee.fromString(string)
print(e2.name)
print(e2.sallary)
