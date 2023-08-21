class Human:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name


# --------------------setting and getting attributes --------------------
guido = Human("Guido")
print(guido.species)
print(guido.name)
print

print("---------------Changing species and name using dot notation----------")
guido.species = "bahal wax cuna"
guido.name = "Abduido"
print(guido.species)
print(guido.name)
print("------------Adding new attributes using dot notation-------------")
guido.nationlaity = "Somali"
print(f"nationlaity: {guido.nationlaity}")

print("------------using built in attribute functins-------------")
# getting attr
print(getattr(guido, "name"))
skin_tone = "dark"
print(f" attr ! exist: {getattr(guido, skin_tone, False)}")
# setting attr
setattr(guido, "height", " 1.83 meter")
# check if instance has attr height
print(f" does have height: {hasattr(guido, 'height')}")
# check if it exists in the dict
print(guido.__dict__)

# ----------------------- P R O P E R T I E S ---------------------------
guido.age = False
print(guido.age)
