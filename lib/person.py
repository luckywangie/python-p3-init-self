class Person:
    def __init__(self, name):
        self.name = name


#test
if __name__ == "__main__":
    person1 = Person("John Doe")
    print(f"The person's name is {person1.name}")