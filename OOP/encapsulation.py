class Person:
    ages = []
    salary = 35000
    def __init__(self, name: str, surname: str):
        self.__name = name ## private
        self._surname = surname # protected
    def greet(self):
        print(f"Hello, my name is {self.__name}")
    
    @staticmethod
    def bye():
        print('this is static method')
    
    @classmethod
    def average_age(self):
        print("sum of all ages",sum(self.ages))
    
    @classmethod
    def set_ages(self, ages):
        self.ages += ages
        print('ages are', self.ages)
    
    @classmethod
    def change_salary(self, new_salary):
        self.salary = new_salary

class Employee(Person):
    def __init__(self, name, surname, salary):
        super().__init__(name,surname)
        self.salary = salary

    def intro(self):
        print(f"Hello it is Employee {self._surname}")

person1 = Person(name='Samandar', surname='Xojiev')
employee = Employee(name='Samandar', surname='Xojiev', salary=4000)
employee.intro()
print(person1._surname)
print(person1.salary)
person2 = Person(name='Ravshan', surname='Kodirov')
print(person1.salary)

Person.change_salary(new_salary=40000)



# While both static methods and class methods are similar 
# in that they can be called without an instance of the class,
#  there are some differences between them:

# Scope of method arguments: A static method does not take the class or instance as an argument, 
# whereas a class method takes the class itself as the first argument.

# Access to class-level attributes: A static method cannot access or modify class-level attributes,
#  whereas a class method can access and modify them.