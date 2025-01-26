class Vehicle:

    # Атрибут класса __COLOR_VARIANTS, текущие цвета автомобиля
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        # Атрибут owner (владелец), который может изменяться
        self.owner = owner
        # Скрытые атрибуты, которые нельзя изменять напрямую
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    # Метод для получения модели транспорта
    def get_model(self):
        return f"Модель: {self.__model}"

    # Метод для получения мощности двигателя
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    # Метод для получения цвета транспорта
    def get_color(self):
        return f"Цвет: {self.__color}"

    # Метод для изменения цвета транспорта
    def set_color(self, new_color):
        # Проверка на наличие нового цвета в списке __COLOR_VARIANTS
        if new_color.lower() in map(str.lower, self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

    # Метод для вывода информации о транспортном средстве
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")


# Класс Sedan, наследуется от класса Vehicle
class Sedan(Vehicle):
    # Константный атрибут класса, лимит пассажиров
    __PASSENGERS_LIMIT = 5


# Создание объекта класса Sedan
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
