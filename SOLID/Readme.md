[GPT Link](https://chatgpt.com/share/675d0220-00f0-800a-b267-024fc9e13ae3)

# SOLID Principles:
The SOLID principles in software engineering are a set of design guidelines that help developers build maintainable, scalable, and robust software systems. They were introduced by Robert C. Martin (Uncle Bob) and are widely used in object-oriented programming (OOP). The principles aim to make code easier to understand, modify, and extend without introducing bugs. Each letter in SOLID represents a principle:

### Single Responsibility Principle

The Single Responsibility Principle (SRP) is one of the SOLID principles in software engineering. It states:

"A class should have only one reason to change."

In other words, a class should only be responsible for one specific part of the functionality of a system. If a class has multiple responsibilities, changes in one responsibility can affect the other, leading to tight coupling and reduced maintainability

### Open-Close Principle:
The Open/Closed Principle (OCP) states that a class should be open for extension but closed for modification. This means you can add new functionality to a class by extending it, rather than modifying its existing code. This principle helps in maintaining existing behavior while allowing new features to be added, making the codebase more robust and easier to maintain.

### Liskov Substitution Principle
The Liskov Substitution Principle (LSP) is a foundational principle of object-oriented programming and one of the SOLID principles. It states:

"Subtypes must be substitutable for their base types."

In other words, objects of a derived class should be able to replace objects of the base class without altering the correctness of the program. This ensures that the behavior of a program remains consistent when using polymorphism.


### Interface Segregation Principle.
The Interface Segregation Principle (ISP) is one of the SOLID principles in object-oriented programming. It states:

"A class should not be forced to implement interfaces it does not use."

In simpler terms, ISP advises creating small, specific interfaces rather than a single, large, general-purpose interface. This ensures that classes only need to implement methods that are relevant to their functionality, avoiding unnecessary dependencies.

### Dependency Injection
Dependency Injection (DI) is a design pattern used to achieve Dependency Inversion, one of the SOLID principles. It allows a class to depend on abstractions (interfaces) instead of concrete implementations, improving flexibility, testability, and maintainability.

In DI, dependencies (objects a class depends on) are provided to a class by an external entity (often a framework or container) rather than the class creating them itself. This decouples the creation of dependencies from their usage.