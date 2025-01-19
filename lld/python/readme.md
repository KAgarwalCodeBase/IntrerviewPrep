Table of Contents
- [Metaclass In Python](#metaclass-in-python)
- [Singleton Pattern](#singleton-pattern)
- [Strategy Pattern](#strategy-pattern-in-python)
- [Observer Pattern](#observer-pattern)
- [Abstract Factory Pattern](#abstract-factory-design-pattern)
- [Builder Pattern](#builder-pattern)
- [Prototype Pattern](#prototype-pattern)
- [Decorator Pattern](#decorator-pattern)
- [State Pattern](#state-pattern)
- [Factory Pattern](https://chatgpt.com/share/678d6247-e9c8-8001-a4f0-385995085a1d)

## Metaclass in Python

1. **Definition**: A metaclass is a class of a class that controls how classes are created and behave. The default metaclass in Python is `type`.

2. **Purpose**:  
   - Customize class creation (`__new__`) and initialization (`__init__`).  
   - Manage class-level behaviors like enforcing patterns (e.g., Singleton).

3. **Key Methods**:
   - `__new__(cls, name, bases, dct)`: Creates the class object itself.
   - `__call__(cls, *args, **kwargs)`: Handles object instantiation when a class is called.

4. **Relationship**:
   - `object` is the base class for all classes.
   - `type` is a metaclass that creates classes, including `object`.
   - `type` is both an instance and a subclass of `object`.

5. **Common Use Cases**:
   - Enforcing design patterns (e.g., Singleton).
   - Validating class definitions.
   - Automatically injecting attributes or methods into classes.

6. **Difference from Abstract Class**:
   - Metaclasses control **class creation**, while abstract classes define a blueprint for subclasses with mandatory method implementation. Abstract classes are comparable to Python’s `abc.ABC`.

---

### Example: Singleton Using Metaclass
```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass
```

This approach centralizes the singleton logic using a metaclass for reusability and scalability.

## Singleton Pattern

## [Strategy Pattern In Python](https://chatgpt.com/share/678c1923-6f1c-8001-b668-bd2334a0d155)
Components of Strategy Pattern:  
- Context: The class that uses a Strategy object.
- Strategy: An interface (or abstract class) that defines a common method signature for all supported algorithms.
- ConcreteStrategy: A class that implements the Strategy interface and provides a specific implementation of an algorithm.

Example: Sorting Strategy

## [Observer Pattern](https://chatgpt.com/share/678d54fa-7a50-8001-8c7a-ae06d9a10a1b)
Components of the Observer Pattern:
- Subject: The object whose state is being observed. It maintains a list of observers and notifies them of any changes.
- Observer: An object that wants to be notified of changes in the subject's state.
- ConcreteSubject: A subclass of the Subject, which holds the state and triggers notifications.
- ConcreteObserver: A subclass of the Observer, which reacts to state changes in the Subject.

# [Builder Pattern](https://chatgpt.com/share/678d5ba1-bab8-8001-a5d3-ff22fad98b46)
Key Components
- Builder: An abstract interface defining the building steps.
- ConcreteBuilder: Implements the Builder interface and provides specific implementations for the construction process.
- Director: Manages the construction process using a Builder object.
- Product: The final object being constructed.

# [Decorator Pattern](https://chatgpt.com/share/678d7207-95b0-8001-b897-539fdddc5cfc)
Key Concepts of Decorator Pattern
- Component: Defines the interface for objects that can have responsibilities added to them dynamically.
- ConcreteComponent: A class that implements the Component interface and represents the core object.
- Decorator: An abstract class implementing the Component interface, containing a reference to a Component object. This class provides the base for adding additional functionalities.
- ConcreteDecorator: A subclass of Decorator that extends the functionality of the Component.

## [State Pattern](https://chatgpt.com/share/678d7f60-1838-8001-bfe5-ca98193c1c9e)
Key Concepts
- Context: The object that has an internal state and delegates behavior to the current state object.
- State Interface/Abstract Class: Defines the common interface for all concrete state classes.
- Concrete States: Implement different behaviors associated with a particular state of the context.
