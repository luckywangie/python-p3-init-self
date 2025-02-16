class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed


#test
if __name__ == "__main__":
    fido = Dog("Fido", "Golden Retriever")
    print(f"{fido.name} is a {fido.breed}")