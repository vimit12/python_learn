class TestClass:
    a = 10
    __e = "Test me"
    def __init__(self, b, c, d):
        self._a = b
        self.__c = c
        self.d = d


    def show_class_name(self):
        print("Class name:", self.__class__.__name__)
        return self.__class__.__name__


def main():
    obj = TestClass(1,2,3)
    print(obj.__dict__)
    obj._TestClass__c = 20
    print(obj._TestClass__c)
    print(obj.__dict__)
    print(TestClass.a, obj._TestClass__e)
    obj._TestClass__e = "Call me"
    print(obj.__dict__)
    print(obj.show_class_name())


if __name__ == '__main__':
    main()