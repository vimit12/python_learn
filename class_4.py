class Student:
    total_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
        Student.total_students += 1

    def __del__(self):
        print(f"Deleting {self.name}'s instance")
        Student.total_students -= 1

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, grades={self.grades})"

    def add_grade(self, grade):
        self.grades.append(grade)

    @classmethod
    def get_total_students(cls):
        return cls.total_students

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __call__(self):
        print(f"{self.name} is being called!")

    def __getitem__(self, index):
        return self.grades[index]

    def __len__(self):
        return len(self.grades)

    def __contains__(self, grade):
        return grade in self.grades

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __add__(self, other):
        total_grades = self.grades + other.grades
        return Student(f"{self.name} {other.name}", (self.age + other.age) // 2)

    def __call__(self):
        print(f"{self.name} is being called!")

    def __getattr__(self, name):
        return f"{name} attribute does not exist"

    def __setattr__(self, name, value):
        if name == "age":
            if value < 0:
                raise ValueError("Age must be positive")
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name == "age":
            raise AttributeError("Cannot delete age attribute")
        del self.__dict__[name]

    def __getitem__(self, key):
        return self.__dict__.get(key, "Key not found")

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        if key == "age":
            raise KeyError("Cannot delete age key")
        del self.__dict__[key]

def main():
    # Creating instances
    student1 = Student("Alice", 20)
    student2 = Student("Bob", 22)

    # Adding grades
    student1.add_grade(85)
    student2.add_grade(78)

    # Using special methods
    print(student1)
    print(student2)
    print(repr(student1))
    print(repr(student2))

    # Using class method
    print("Total students:", Student.get_total_students())

    # Using static method
    print("Is Alice an adult?", Student.is_adult(student1.age))
    print("Is Bob an adult?", Student.is_adult(student2.age))

    # Using operator overloading
    combined_student = student1 + student2
    print("Combined student:", combined_student)

    # Using __call__ method
    student1()

    # Using __getitem__ and __len__ methods
    print(student1[0])
    print(len(student1))

    # Using comparison methods
    print(student1 == student2)
    print(student1 != student2)
    print(student1 < student2)
    print(student1 <= student2)
    print(student1 > student2)
    print(student1 >= student2)

    # Using __getattr__, __setattr__, __delattr__
    print(student1.non_existent_attribute)
    student1.dynamic_attribute = "Dynamic Value"
    print(student1.dynamic_attribute)
    del student1.dynamic_attribute

    # Using __getitem__, __setitem__, __delitem__
    print(student1["non_existent_key"])
    student1["new_key"] = "New Value"
    print(student1["new_key"])
    del student1["new_key"]


if __name__ == '__main__':
    main()
    