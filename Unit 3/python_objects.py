# Pyhton objects are digital represnetation of things
# that can interact with one another

# Objects are collection of data that we use tp
# characterize things.

# Example - A car is a object/ "Thing"
# characteristics of a car: engine, tires, battery, seats,
# color, model, doors

# when we want to make an object, we need to use a class
# class keyword = object maker

# the class name ALWAYS is capitalized / Pascal Case
class Car:
    # we ALWAYS stat with this code below
    # this function is use to describe the characteristics of
    # the object ex. self
    def __intit__(self, color, year, model, engine, pushToStart):
        # attributes - the characteristics that describe an object
        # generally it will be the basic data types
        self.color ="red",
        self.year = 2027,
        self.model = "enzo",
        self.engine = "V12",
        self.pushToStart = True

        # Methods - functions ("that exist insdie of a object")
        # these are functions that exclusively work within the object
        # Things the car actually does!

        def start():
            # if key is present when push to start is clicked/ pressed, 
            # start the engine and vehicle
            if self.pushToStart == True:
                # start car
        
        def accelerate():
            # when gas pedal is pressed, move vehicle.

        def brake():
            # when brake pedal is pressed, trigger braking pads and lock


class Character_GTA:
    def__init__(self):
    # attributes - characteristics
    self.movementspeed = 5
    self.inventory =
    # methods - what it does/ its actions
    def run():
        # when x button is clicked, increase movement by 5
        self.movementSpeed +=5


    def addItemToInventory():
        #when right trigger is pressed and nerby another object
        self.inventory.append("sword")