class Parent1:
    def __init__(self, param1):
        self.param1 = param1

    def show(self):
        print(f"Parent1: param1 = {self.param1}")


class Parent2:
    def __init__(self, param2):
        self.param2 = param2

    def show(self):
        print(f"Parent2: param2 = {self.param2}")


class Child(Parent1, Parent2):
    def __init__(self, param1, param2, param3):
        super().__init__(param1)  # Initialize Parent1's parameter
        Parent2.__init__(self, param2)  # Initialize Parent2's parameter
        self.param3 = param3

    def show(self):
        super().show()  # Call Parent1's show() method using super()
        Parent2.show(self)
        print(f"Child: param3 = {self.param3}")


# Creating an instance of Child
child = Child("Value1", "Value2", "Value3")

# Calling the show() method of Child
child.show()
