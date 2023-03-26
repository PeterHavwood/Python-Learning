# Use __slots__ to strict the properties of an instance of certain class
class Student(object):
    __slots__ = ('name','major','age','setAge')

def setAge(self, age):
    self.age = age

s = Student()
s.name = 'Peter'
s.major = 'History'
# s.gender = 'male' is invalid
Student.setAge = setAge
s.setAge(10)
print(s.age)