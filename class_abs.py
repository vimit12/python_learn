from abc import ABCMeta, abstractclassmethod


class Jungle(metaclass=ABCMeta):

    def __init__(self, name=None):
        self.name = name

    @abstractclassmethod
    def scarySound(self):
        pass


class Lion(Jungle):
    def scarySound(self):
        print("ROAR " * 10)

#return object string
class StringObject:

    def __str__(self):
        return "<Str obj return>"


def main():
    lion = Lion()
    lion.scarySound()

    str_obj = StringObject()
    print(str_obj, type(str_obj))


if __name__ == '__main__':
    main()
