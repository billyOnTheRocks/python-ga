class Animal:
    def __init__(self):
        print("Animal created")

        def who(self):
            print("Animal")

        def eat(self):
            print("Eating")

class Dog(Animal):
    def __init__ (self):
        super().__init__()
        print("Dog created")

    def who(self):
        print("Animal")

    def bark(self):
        print("woof")


def main():
    sam = Dog()


if __name__=='__main__':
   main()
