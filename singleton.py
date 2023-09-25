class SingleToneClass:
    __instance__ = None

    def __init__(self) -> None:
        
        if SingleToneClass.__instance__ is None:
            SingleToneClass.__instance__ = self
        else:
            raise Exception("We cannot create another class object.")
        
    
    @staticmethod
    def get_instance():

        if not SingleToneClass.__instance__:
            SingleToneClass()
        
        return SingleToneClass.__instance__
    

# Creating an object of above defined class.  
obj1 = SingleToneClass()  
print(obj1)  


obj2 = SingleToneClass.get_instance()
print(obj2)


obj3 = SingleToneClass.get_instance()
print(obj3)

print(obj4)  
obj4 = SingleToneClass()  