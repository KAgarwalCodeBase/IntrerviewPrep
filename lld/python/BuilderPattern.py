from abc import ABC, abstractmethod
# Product: The complex object
class House:
    def __init__(self):
        self.floors = None
        self.walls = None
        self.roof = None
    
    def __str__(self):
        return f"House with {self.floors} floors, {self.walls} walls, and a {self.roof} roof."

# Abstract Builder
class HouseBuilder(ABC):
    @abstractmethod
    def set_floors(self, floors):
        pass
    @abstractmethod
    def set_walls(self, walls):
        pass
    @abstractmethod
    def set_roof(self, roof):
        pass

# Concrete House Builder
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()
    def set_floors(self, floors):
        self.house.floors = floors 
        return self
    def set_walls(self, walls):
        self.house.walls = walls 
        return self
    def set_roof(self, roof):
        self.house.roof = roof
        return self
    def get_result(self):
        return self.house

# Director
class Director:
    def __init__(self, builder):
        self.builder = builder
    def construct_simple_house(self):
        print('Building a Simple House:')
        self.builder.set_floors(1).set_walls('brick').set_roof('wooden')
        return self.builder.get_result()

    def construct_luxury_house(self):
        print("Building a Luxury House:")
        self.builder.set_floors(3).set_walls('glass').set_roof('slate')
        return self.builder.get_result()
    
# Client Code    
if __name__=='__main__':
    builder = ConcreteHouseBuilder()
    director = Director(builder)

    simple_house = director.construct_simple_house()
    print(simple_house)
    luxury_house = director.construct_luxury_house()
    print(luxury_house)