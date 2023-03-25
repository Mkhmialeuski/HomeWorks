class Triangle:
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c

    def check(self):
        if self.__a + self.__b > self.__c and self.__a + self.__c > self.__b and self.__b + self.__c > self.__a:
            return True
        else:
            print('не может быть такого треугольника')
            return False

    def get_type(self):
        if self.__a == self.__b and self.__a == self.__c:
            print('равносторонний')
        elif self.__a == self.__b or self.__a == self.__c or self.__b == self.__c:
            print('равнобедренный')
        else:
            if self.__c ** 2 > (self.__a **2) + (self.__b ** 2) or self.__b ** 2 > (self.__a **2) + (self.__c ** 2) or self.__a ** 2 > (self.__b **2) + (self.__c ** 2):
                print('тупоугольный')
            elif self.__c ** 2 == (self.__a ** 2) + (self.__b ** 2) or self.__b ** 2 == (self.__a ** 2) + (self.__c ** 2) or self.__a ** 2 == (self.__b ** 2) + (self.__c ** 2):
                print('прямоугольный')
            else:
                print('остроугольный')




a = Triangle(13,11,20)
if a.check():
    a.get_type()
