
class Calculator:

    def __init__(self, brand, price, serial_number):

        self.brand = brand
        self.price = price
        self.serial_number = serial_number
        self.__usage_odometer = 0
        self.__battery = 100

    def __repr__(self):
        return f'Marka {self.brand}, cena: {self.price}, numer seryjny: {self.serial_number}\naktualny stan licznika {self.__usage_odometer}'

    @property
    def get_stats(self):
        return self.__usage_odometer, self.__battery

    def __update_stats(self):
        self.__battery -= 0.5
        self.__usage_odometer += 1

    def sum(self, a, b):
        self.__update_stats()
        return a + b

    def sub(self, a, b):
        self.__update_stats()
        return a - b

    def mul(self, a, b):
        self.__update_stats()
        return a * b

    def div(self, a, b):
        self.__update_stats()
        try:
            return a / b
        except ZeroDivisionError as e:
            print(e)

    def pow(self, a, b):
        self.__update_stats()
        return a ** b

my_calc = Calculator("Casio", "150 $", "XDC-1A23")

print(my_calc)

# print(my_calc.brand)
# print(my_calc.price)
# print(my_calc.serial_number)

a = int(input(f"Podaj perwsza liczbe: "))
b = int(input(f"Podaj druga liczbe: "))


print(my_calc.sum(a,b))
print(my_calc.sub(a,b))
print(my_calc.mul(a,b))
print(my_calc.div(a,b))
print(my_calc.pow(a,b))

print(f"actualny stan licznika po obliczeniach: {my_calc.get_stats}")