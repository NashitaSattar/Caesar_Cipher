def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet_with("Nashita", "Waterloo") #positional arguments depend on the position of the parameter

greet_with(location = "Bikini Bottom", name = "Bobby Sue") #keyword arguments are the same even if you change the position
