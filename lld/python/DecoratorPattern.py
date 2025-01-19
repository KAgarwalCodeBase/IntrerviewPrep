from abc import ABC, abstractmethod

# Component interface
class Pizza(ABC):
    @abstractmethod
    def getDescription(self)->str:
        pass
    def getCost(self)->float:
        pass

# ConcreteComponent
class MargheritaPizza(Pizza):
    def getDescription(self) -> str:
        return "Margherita Pizza"
    def getCost(self) -> float:
        return 5.0

# Decorator
class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza 
    
    @abstractmethod
    def getDescription(self) -> str:
        pass 
    
    @abstractmethod
    def getCost(self)-> float:
        pass 

# ConcreteDecorator
class Cheese(ToppingDecorator):
    def getDescription(self):
        return self._pizza.getDescription() + ", Cheese"
    def getCost(self):
        return self._pizza.getCost() + 1.5


class Olives(ToppingDecorator):
    def getDescription(self):
        return self._pizza.getDescription() + ", Olives"
    def getCost(self):
        return self._pizza.getCost() + 0.7

class Pepperoni(ToppingDecorator):
    def getDescription(self):
        return self._pizza.getDescription() + ", Pepperoni"
    def getCost(self):
        return self._pizza.getCost() + 2.0

# Controller
if __name__=="__main__":
    pizza = MargheritaPizza()
    print(f"{pizza.getDescription()} Cost: ${pizza.getCost()}")
    
    pizza_with_cheese = Cheese(pizza)
    print(f"{pizza_with_cheese.getDescription()} Cost: ${pizza_with_cheese.getCost()}")
    
    pizza_with_cheese_olives = Olives(pizza_with_cheese)
    print(f"{pizza_with_cheese_olives.getDescription()} Cost: ${pizza_with_cheese_olives.getCost()}")
    
    # adding pepperoni on top of everything
    deluxe_pizza = Pepperoni(pizza_with_cheese_olives)
    print(f"{deluxe_pizza.getDescription()} Cost: ${deluxe_pizza.getCost()}")
    