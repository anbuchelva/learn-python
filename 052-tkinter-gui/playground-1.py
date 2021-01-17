################################
# examples of args and kwargs. #
################################

# *args will get n number inputs
def add(*args):
    # args are tuples
    # print(type(args))
    sum = 0
    for num in args:
        sum += num
    print(sum)


add(1, 2, 3, 4, 10)


# **kwargs will get n number of inputs as keyword arguments
def calculate(**kwargs):
    # kwargs are dictionaries
    # print(type(kwargs))
    # print(kwargs)
    
    # for (item, value) in kwargs.items():
    #     print(item)
    #     print(value)    
    
    n = 2
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(add= 3, multiply= 5)


# example for creating a class with kw args.
class Car:
    def __init__(self, **kw):
        # get() can be used to get the values of a dict. 
        # if the key is not present, it gives output as 'None'
        self.model = kw.get("model")
        self.make = kw.get("make")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Maruti", model="Swift")
print(my_car.model)
print(my_car.color)
