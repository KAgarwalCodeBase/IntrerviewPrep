# Table of Contents
-  [Encapsulation](#encapsulation-its-protect-our-data)
- [Inheritance](#inheritance)
- [Strategy Pattern](#strategy-pattern)
- [Observer Pattern](#observer-pattern)
- [Abstract Factory Pattern](#abstract-factory-design-pattern)
- [Singleton Pattern](#singleton-pattern)
- [Builder Pattern](#builder-pattern)
- [Prototype Pattern](#prototype-pattern)
- [Decorator Pattern](#decorator-pattern)
- [State Pattern](#state-pattern)

<!-- State, Factory, Decorator, Command. -->

## Encapsulation: It's protect our data.
```
class Dog{
    String name;
    double height;

    setWeight(int newWeight){
        if(newWeight > 0){
            weight = newWeight;
        }else{
            // Throw an error
        }
    }
}
```

`Instance variable` is created inside the class.

`Local variable` is created inside the methods.

<sub>[back to top](#table-of-contents)</sub>

## Inheritance
![Inheritance1](./assets/inheritance1.png)
![Inheritance1](./assets/inheritance2.png)
![Inheritance1](./assets/inheritance3.png)


### We cann't use non-static variable and methods inside static method.

<sub>[back to top](#table-of-contents)</sub>

## Strategy Pattern
- In strategy pattern we mainly uses concept of decoupling.
- Where instead of implementing the interface we uses composition for adding the functionality.
- Not implementing interface because then all classes should have to implement it even they are not using it.

<sub>[Code Link](https://www.newthinktank.com/2012/08/strategy-design-pattern-tutorial/) |</sub> 
<sub>[back to top](#table-of-contents)</sub>

## Observer Pattern
**Subject.java (interface)**
- public void register(Observer o);
- public void unregister(Observer o);
- public notifyAll();

**Observer.java (interface)**
- public update(params...);

Subject will register all the observers and notify them if its internal state changes.

<sub>[Code Link](https://www.newthinktank.com/2012/08/observer-design-pattern-tutorial/) |</sub> 
<sub>[back to top](#table-of-contents)</sub>

## [Abstract Factory Design Pattern](https://chatgpt.com/share/6766515c-b660-8008-b475-9cce6d44e9f0)
Provide an interface of creating families of related or dependent objects without specifying their concrete classes.

Example: In a company manager knows who can solve the issue. And then he refers to the concerned department.

<sub>[back to top](#table-of-contents)</sub>

## [Singleton Pattern](https://chatgpt.com/share/67665514-ca50-8008-b656-bcfa3c00b3c5)
Use for creating a single instance of an object.

Example: Singleton Pattern
```java
public class Singleton {
    private static Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton(); // Lazy initialization
        }
        return instance;
    }
}
```

Thread safe singleton class.
```java
public class Singleton {
    private static volatile Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

<sub>[back to top](#table-of-contents)</sub>

## [Builder Pattern](https://youtu.be/9XnsOpjclUg?si=a0VtB4Tp0aR3KKEm)

The Builder Pattern is a creational design pattern used in software development to construct complex objects step by step. It provides a way to build objects that might require multiple steps or components, without needing to directly call the constructor or know all the intricate details of object creation.
- Pattern used to create objects made from a bunch of other objects.
- When you want to build an object made up from other objects.
- When you want the creation of these parts to be independent of the main object.
- Hide the creation of the parts from the client so both aren't dependent.
- The builder knows the specifics and nobody else does.

Robot->RobotBuilder->RobotEngineer

<sub>[Code Link](https://www.newthinktank.com/2012/09/builder-design-pattern-tutorial/) |</sub> 
<sub>[back to top](#table-of-contents)</sub>

## [Prototype Pattern](https://youtu.be/AFbZhRL0Uz8?si=Sx-JHwlswc6EYutU)
- Creating new objects (instances) by cloning (copying) other objects.
- Allows for adding of any subclass instance of a known super class at run time.
- When there are numerous potential classes that you want to only use if needed at runtime
- Reduces the need for creating subclasses

Object Cloing using serializable keyword.

<sub>[back to top](#table-of-contents)</sub>

## [Decorator Pattern](https://www.youtube.com/watch?v=j40kRwSm4VE&list=PLF206E906175C7E07&index=11&ab_channel=DerekBanas)
The **Decorator Pattern** is a **structural design pattern** used to dynamically add behavior or responsibilities to an object without modifying its code. It allows you to attach additional functionality to an object by wrapping it in a decorator class.

### Key Characteristics
1. **Flexible Alternative to Subclassing**:
   - Instead of extending a class to add functionality, the decorator pattern allows composition, making it more flexible.
2. **Dynamic Behavior Addition**:
   - New behaviors can be added to objects at runtime.
3. **Open/Closed Principle**:
   - You can extend the functionality of an object without modifying its original implementation.

---

### Structure of the Decorator Pattern
1. **Component**:
   - Defines the interface or abstract class for objects that can have responsibilities added to them.
2. **Concrete Component**:
   - The base implementation of the component interface, representing the primary object.
3. **Decorator**:
   - An abstract class that implements the component interface and wraps a component object.
4. **Concrete Decorators**:
   - Specific implementations of the decorator that add or override behavior.

---

### Benefits of Decorator Pattern
1. **Flexibility**:
   - Combine multiple decorators to customize an object.
2. **Open/Closed Principle**:
   - Add new behaviors without modifying existing classes.
3. **Runtime Customization**:
   - Apply different decorators dynamically during program execution.

---

### When to Use
- When you need to add or modify the behavior of objects dynamically.
- When subclassing is impractical or leads to an explosion of subclasses to handle every possible combination of behavior.
- When you want to create an extensible design for adding responsibilities.

PlainPizze->ToppingDecorator(Mozzarella, TomatoSauce etc)
Both extending and creating composite object in ToppingDecorator.

<sub>[Code Link](https://www.newthinktank.com/2012/09/decorator-design-pattern-tutorial/) |</sub> 
<sub>[back to top](#table-of-contents)</sub>

## State Pattern

The **State Pattern** is a **behavioral design pattern** that allows an object to change its behavior when its internal state changes. It encapsulates state-specific behavior into separate classes and delegates state transitions to these classes. 

---

### **Key Characteristics**
1. **Encapsulation of State-Specific Behavior**:
   - Different states are represented by different classes.
2. **State Transition Logic**:
   - The object delegates state-related behavior to the current state object.
3. **Open/Closed Principle**:
   - Adding new states requires creating new classes without modifying existing ones.

---

### **Structure of State Pattern**

1. **Context**:
   - Maintains a reference to the current state and delegates requests to the state object.

2. **State Interface**:
   - Defines the interface for all state-specific behavior.

3. **Concrete States**:
   - Implement the state-specific behavior and handle state transitions.

---

### **Example**

#### Traffic Light Example

```java
// State Interface
interface TrafficLightState {
    void handleState(TrafficLight context);
}

// Concrete States
class RedLight implements TrafficLightState {
    @Override
    public void handleState(TrafficLight context) {
        System.out.println("Red Light: Stop!");
        context.setState(new GreenLight());
    }
}

class GreenLight implements TrafficLightState {
    @Override
    public void handleState(TrafficLight context) {
        System.out.println("Green Light: Go!");
        context.setState(new YellowLight());
    }
}

class YellowLight implements TrafficLightState {
    @Override
    public void handleState(TrafficLight context) {
        System.out.println("Yellow Light: Slow down!");
        context.setState(new RedLight());
    }
}

// Context
class TrafficLight {
    private TrafficLightState state;

    public TrafficLight() {
        this.state = new RedLight(); // Initial state
    }

    public void setState(TrafficLightState state) {
        this.state = state;
    }

    public void changeState() {
        state.handleState(this);
    }
}

// Client
public class StatePatternExample {
    public static void main(String[] args) {
        TrafficLight trafficLight = new TrafficLight();

        // Simulate traffic light changes
        trafficLight.changeState(); // Red to Green
        trafficLight.changeState(); // Green to Yellow
        trafficLight.changeState(); // Yellow to Red
    }
}
```

---

### **Output**
```
Red Light: Stop!
Green Light: Go!
Yellow Light: Slow down!
```

---

### **Benefits of State Pattern**
1. **Improved Maintainability**:
   - State-specific behavior is localized to individual state classes.
2. **Open/Closed Principle**:
   - Adding new states is easy and doesn't require modifying existing code.
3. **Eliminates Complex Conditional Logic**:
   - Avoids large `if-else` or `switch` statements.

---

### **Use Cases**
- Objects that have complex state-dependent behavior.
- Systems requiring clear separation of state logic (e.g., traffic lights, finite state machines, media players).
- When behavior changes dynamically at runtime based on the object's state.

<sub>[back to top](#table-of-contents)</sub>
