#!python3
"""
Creating the parts of a class
"""

# An object is created with a class definition.  It can be considered
# a mini program with its own variables (properties) and functions(methods)
class dog:
    # variables created inside the class are properties that ALL instances
    # of the object will have
    name = ""
    hair = ""
    breed = ""
    age = 0
    legs = 4
    tail = True

    # A constructor is a specific function that will be run every
    # time a new instance is created.  It can have input parameters.
    # Note that the first input parameter is required to be "self"
    def __init__(self, name, gender, hair, breed, age, legs=4, tail = True):
        # At any time, we can access variables/properties of the class object
        # Note the use of the "self." prefix, whereas variables that do not
        # contain the prefix are local variables
        self.name = name
        self.gender = gender
        self.hair = hair
        self.breed = breed
        self.age = age
        self.legs = legs
        self.tail = tail
        print("I have a new dog named " + self.name)
        
    def commands(self):
        # Note that any function/method definition must include
        # self as its first parameter.  So a function that takes
        # no input parameters is actually required to have 1
        print("------------------------")
        print("Do you want your dog to:")
        print("1.Bark")
        print("2.Roll Over")
        print("3.Play Dead")
        print("4.Bye")
        command = input("Choose a number[1-4]:")
        print("")
        return int(command)
    
    def doggyDoes(self,command):
        # Note this method has self and an additional parameter
        # this means that the method actually requires 1 input parameter
        if command == 1:
            self.bark()
        elif command == 2:
            self.rollover()
        elif command == 3:
            self.playdead()

    def bark(self):
        print("bark!")

    def rollover(self):
        print(self.name + " wags his tail and rolls over!")

    def playdead(self):
        print(self.name + " lies down and doesn't move")

    def __del__(self):
        # This is a destructor.  It is a function that contains code to be
        # executed when the object is destroyed.
        print("Goodbye " + self.name + ", it was nice knowing you\n")



def main():
    # An instance of the object is instantiated by assigning the
    # class to a name like a variable.  Any input parameters
    # required by the constructor are included as parameters of the class
    rover = dog("Rover","male","brown","Shepherd",4)

    while True:
        command = rover.commands()
        if command == 4:
            # An instance can be destroyed or deleted using the del command
            del rover
            break
        rover.doggyDoes(command)

        print("\n")

if __name__ == "__main__":
    main()
