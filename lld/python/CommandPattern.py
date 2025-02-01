from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass 

    @abstractmethod
    def undo(self):
        pass 

# ConcreteCommand: Truns the light on
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()
    
    def undo(self):
        self.light.turn_off()

# ConcreteCommand: Turns the light off
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# Receiver: Light
class Light:
    def turn_on(self):
        print("The light is on.")
    
    def turn_off(self):
        print("The light is off.")

# Invoker: Remote Control
class RemoteControl:
    def __init__(self):
        self.command = None 
    
    def set_command(self, command):
        self.command = command 

    def press_button(self):
        if self.command:
            self.command.execute()

    def press_undo(self):
        if self.command:
            self.command.undo()

if __name__=="__main__":
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()

    # Turn the light on
    remote.set_command(light_on)
    remote.press_button()

    # Undo the action
    remote.press_undo()

    # Turn the light off
    remote.set_command(light_off)
    remote.press_button()

    # Undo the action
    remote.press_undo()
