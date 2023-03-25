class Circle:
    def __init__(self,radius):
        self.__radius = radius

    def get_area(self):
        return 3.14 * (self.__radius**2)

    def get_circumference(self):
        return 2 * 3.14 * self.__radius

    def set_input(self,x):
        x = input()
        if isinstance(x, str):
            try:
                x = int(x)
                if x > 0:
                    self.__radius = x
                    return self.__radius
            except Exception:
                x = 2
                self.__radius = x
                return self.__radius

cir = Circle(6)
print(cir.get_area())
cir.set_input(3)
print(cir.get_area())
# print(cir.get_circumference())

