

class house:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __del__(self, *args):
        print(f'{self.args[0]} снесён, но он останется в истории' )

h1 = house('ЖК Эльбрус', 10)
print(house.houses_history)
h2 = house('ЖК Акация', 20)
print(house.houses_history)
h3 = house('ЖК Матрёшки', 20)
print(house.houses_history)

# Удаление объектов
del h2
del h3

print(house.houses_history)


