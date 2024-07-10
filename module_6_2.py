class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.model = __model
        self.color = __color
        self.engine_power = __engine_power

    def set_color(self, new_color):
        new_color = new_color.lower()
        if new_color in self.__COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

    def print_info(self):
        print(f"Владелец: {self.owner}")
        print(f"Модель: {self.model}")
        print(f"Цвет: {self.color}")
        print(f"Мощность двигателя: {self.engine_power}")

class Sedan(Vehicle):
    def __init__(self, owner, __model, __color, engine_power):
        super().__init__(owner, __model, __color, engine_power)

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)


vehicle1.print_info()


vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'


vehicle1.print_info()
