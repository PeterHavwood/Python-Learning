# The object in parentheses means this class inherited from object class
class Student(object): 
    # This property belongs to the class
    count = 0

    # These properties belongs to the instance
    def __init__(self, name, age, major):
        self.name = name
        self.__age = age    # A private property
        self.major = major
        Student.count += 1
    
    def get_age(self):
        return self.__age

    # Use a function to prevent invalid argument
    def set_age(self, age):
        if 10 <= age <= 25:
            self.__age = age
        else:
            raise ValueError('Not a valid number for age')

    # Self is an argument refers to the instance and you dont need pass it when you call the function
    def selfIntroduction(self):
        print(f'Hello! I\'m {self.name} form {self.major}.')

def main():
    print(Student.count)
    Peter = Student('Peter', 18, 'Atmosphere Science')
    print(Student.count)
    Peter.selfIntroduction()
    
    # print(Peter.__age) is invalid
    # Peter.set_age(0) will raise an error
    Peter.set_age(20)
    print(Peter.get_age())


if __name__ == '__main__':
    main()