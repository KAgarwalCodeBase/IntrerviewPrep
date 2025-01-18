from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float):
        pass 

# Concrete Observer
class TemperatureDisplay(Observer):
    def update(self, temperature: float):
        print(f"Temperature Display: Current temperature is {temperature}°C")

class HumidityDisplay(Observer):
    def update(self, temperature: float):
        print(f"Humidity Display: The temperature is {temperature}°C, showing humidity levels.")

# Subject Interface
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass 
    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass 
    @abstractmethod
    def notify_observers(self):
        pass 

# Concrete Subject
class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0.0
    
    def register_observer(self, observer):
        return self._observers.append(observer)
    
    def remove_observer(self, observer):
        self._observers.remove(observer)
    
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature: float):
        print(f"WeatherStation: Temperature set to {temperature}°C")
        self._temperature = temperature
        self.notify_observers()

# Example Usage
if __name__ == "__main__":
    weather_station = WeatherStation()

    # Create Observers (Display)
    temp_display = TemperatureDisplay()
    humidity_display = HumidityDisplay()

    # Register observers
    weather_station.register_observer(temp_display)
    weather_station.register_observer(humidity_display)

    # Change temperature and notify observers
    weather_station.set_temperature(25.5)
    weather_station.set_temperature(30.0)

    # Removing observer
    weather_station.remove_observer(humidity_display)
    weather_station.set_temperature(22.0)
    
