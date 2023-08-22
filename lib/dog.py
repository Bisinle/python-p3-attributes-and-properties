#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer",
]
#!/usr/bin/env python3


class Dog:
    def __init__(self, name="london", breed="Pug"):
        if isinstance(name, str) and (1 <= len(name) <= 25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    @property
    def name(self):
        print(f" accessed {self._name}")
        return self._name

    @name.setter
    def name(self, value):
        print(value)
        if isinstance(value, str) and (1 <= len(value) <= 25):
            print(f"{self._name} is now {value}")
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed_val):
        if isinstance(breed_val, str) and (1 <= len(breed_val) <= 25):
            print(f"{breed_val._breed} is now {breed_val}")
            self._breed = breed_val
        else:
            print("Name must be string between 1 and 25 characters.")


fido = Dog("Carla")  # Corrected: Pass a strinyyyg as the name argument
print(fido.name)
fido.name = "kkkkk"
print(fido.__dict__)
