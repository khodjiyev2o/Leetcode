class Account():
    num_accounts = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.__private_atribute = 10
        self._protected_attribute = 1
        Account.num_accounts += 1

    def __str__(self):
        return f"{self.name}, with  {self.balance}"

    @classmethod
    def obj_static_method_improve_by_10(self):
        self.num_accounts += 10
    @staticmethod
    def obj_static_method():
        print("static method")

    def del_account(self):
        self.num_accounts -= 1

    def deposit(self, amt):
        self.balance = self.balance + amt

    def withdraw(self, amt):
        self.balance = self.balance - amt

    def inquiry(self):
        return self.balance

    def get_private_attr(self):
        print(self.__private_atribute)


a = Account('Samandar', 123000)


class Person(Account):
    def __init__(self, name, balance, first_name):
        super().__init__(name, balance)
        self.first_name = first_name

    def get_protected_attr(self):
        print(self._protected_attribute)

a = Person(name="Damir", balance=2, first_name=2322)
print(a)
a.get_private_attr()
"""

Private methods and attributes are:
1.written with double underscore
2.Cannot be accessed from outside the class itself,even if it is inherited
3. Can be accesse by getter and setter methods
"""


class BaseClass:

    def __init__(self, attribute):
        self.attribute = attribute


class Subclass(BaseClass):
    __slots__ = ['another']
    def __init__(self, attribute, another):
        super().__init__(attribute)
        self.another = another

a = Subclass(attribute='attribute', another=111)