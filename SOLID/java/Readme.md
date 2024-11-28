### Index
- [Marker Interfaces in JAVA](#marker-interfaces-in-java)
- [Order of Execution of Initialization block and constructor](#order-of-execution-of-initialization-block-and-constructor-in-java)
- [Object Class & it's list of method.](#object-class--its-list-of-methods)
- [Clone Method in JAVA](#clone-method-in-java)
- [Transient Fields in JAVA](#transient-fields-in-java)
- [Serialization](#serializationdeserialization-in-java-updated-summary)
- [Atomic, Volatile & Synchronized](#atomic-volatile-and-synchronized)
- [Object Finalization in Java](#object-finalization-in-java)
- [StringBuffer Vs StringBuilder](#stringbuffer-vs-stringbuilder)
- [Comparison of some similar data structures in Java based on functionality, thread-safety, performance, and usage](#comparison-of-some-similar-data-structures-in-java-based-on-functionality-thread-safety-performance-and-usage)

### Marker Interfaces in JAVA
-   Cloneable
- Serializable

[back to top](#index)

### Order of execution of initialization block and constructor in java.

`Parent class static` → `Child class static` → `Parent class instance` → `Parent constructor` → `Child class instance` → `Child constructor`.

[back to top](#index)

### Object Class & it's list of methods.
The **`Object` class** in Java is the root of the class hierarchy. Every class in Java directly or indirectly inherits from the `Object` class, which means every class has access to its methods. Below is a detailed explanation of the methods provided by the `Object` class, with examples.

---

### **List of Java Object Class Methods**

#### 1. **`clone()`**
- **Description**: Creates and returns a copy of the object.
- **Access Modifier**: `protected` (needs to be overridden in the subclass and the class must implement `Cloneable` interface).

**Example**:
```java
class Person implements Cloneable {
    String name;

    Person(String name) {
        this.name = name;
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    public static void main(String[] args) throws CloneNotSupportedException {
        Person p1 = new Person("John");
        Person p2 = (Person) p1.clone();
        System.out.println(p2.name); // Output: John
    }
}
```

---

#### 2. **`equals()`**
- **Description**: Compares two objects for equality. By default, checks reference equality.
- **Override to compare contents**: Often overridden to check logical equality (e.g., for custom objects).

**Example**:
```java
class Person {
    String name;

    Person(String name) {
        this.name = name;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Person person = (Person) obj;
        return name.equals(person.name);
    }

    public static void main(String[] args) {
        Person p1 = new Person("John");
        Person p2 = new Person("John");
        System.out.println(p1.equals(p2)); // Output: true
    }
}
```

---

#### 3. **`finalize()`**
- **Description**: Called by the garbage collector before an object is destroyed.
- **Usage**: Rarely used in modern Java due to inefficiency and unreliability.

**Example**:
```java
class Demo {
    @Override
    protected void finalize() throws Throwable {
        System.out.println("Object is being garbage collected.");
    }

    public static void main(String[] args) {
        Demo d = new Demo();
        d = null; // Mark object for garbage collection
        System.gc(); // Request JVM to perform garbage collection
    }
}
```

---

#### 4. **`getClass()`**
- **Description**: Returns the runtime class of the object.

**Example**:
```java
class Demo {
    public static void main(String[] args) {
        Demo obj = new Demo();
        System.out.println(obj.getClass().getName()); // Output: Demo
    }
}
```

---

#### 5. **`hashCode()`**
- **Description**: Returns a hash code value for the object.
- **Default Behavior**: Returns an integer derived from the memory address of the object.
- **Override it**: When overriding `equals()` for logical equality, override `hashCode()` for consistent behavior in hash-based collections.

**Example**:
```java
class Person {
    String name;

    Person(String name) {
        this.name = name;
    }

    @Override
    public int hashCode() {
        return name.hashCode();
    }

    public static void main(String[] args) {
        Person p1 = new Person("John");
        System.out.println(p1.hashCode()); // Output: Hash code based on name
    }
}
```

---

#### 6. **`notify()`**
- **Description**: Wakes up a single thread waiting on this object's monitor.
- **Usage**: Used in multithreading with synchronized blocks.

**Example**:
```java
class NotifyExample {
    public static void main(String[] args) {
        Object lock = new Object();

        Thread waitingThread = new Thread(() -> {
            synchronized (lock) {
                try {
                    System.out.println("Waiting...");
                    lock.wait();
                    System.out.println("Notified!");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        Thread notifyingThread = new Thread(() -> {
            synchronized (lock) {
                System.out.println("Notifying...");
                lock.notify();
            }
        });

        waitingThread.start();
        notifyingThread.start();
    }
}
```

---

#### 7. **`notifyAll()`**
- **Description**: Wakes up all threads waiting on this object's monitor.

**Example**:
```java
class NotifyAllExample {
    public static void main(String[] args) {
        Object lock = new Object();

        Thread waitingThread1 = new Thread(() -> {
            synchronized (lock) {
                try {
                    System.out.println("Thread 1 waiting...");
                    lock.wait();
                    System.out.println("Thread 1 notified!");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        Thread waitingThread2 = new Thread(() -> {
            synchronized (lock) {
                try {
                    System.out.println("Thread 2 waiting...");
                    lock.wait();
                    System.out.println("Thread 2 notified!");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        Thread notifyingThread = new Thread(() -> {
            synchronized (lock) {
                System.out.println("Notifying all...");
                lock.notifyAll();
            }
        });

        waitingThread1.start();
        waitingThread2.start();
        notifyingThread.start();
    }
}
```

---

#### 8. **`toString()`**
- **Description**: Returns a string representation of the object.
- **Default Behavior**: Class name + `@` + hexadecimal hash code.
- **Override it**: For meaningful string representation.

**Example**:
```java
class Person {
    String name;

    Person(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Person{name='" + name + "'}";
    }

    public static void main(String[] args) {
        Person p = new Person("John");
        System.out.println(p); // Output: Person{name='John'}
    }
}
```

---

#### 9. **`wait()`**
- **Description**: Causes the current thread to wait until another thread invokes `notify()` or `notifyAll()` on the same object.
- **Usage**: Works with `synchronized` blocks to coordinate thread communication.

**Example**:
```java
class WaitExample {
    public static void main(String[] args) {
        Object lock = new Object();

        Thread waitingThread = new Thread(() -> {
            synchronized (lock) {
                try {
                    System.out.println("Waiting...");
                    lock.wait();
                    System.out.println("Notified!");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        Thread notifyingThread = new Thread(() -> {
            synchronized (lock) {
                System.out.println("Notifying...");
                lock.notify();
            }
        });

        waitingThread.start();
        notifyingThread.start();
    }
}
```

---

### **Summary**
| **Method**         | **Description**                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| `clone()`           | Creates a copy of the object (needs `Cloneable` interface).                    |
| `equals()`          | Compares two objects for equality.                                             |
| `finalize()`        | Called by garbage collector before object destruction.                         |
| `getClass()`        | Returns the runtime class of the object.                                       |
| `hashCode()`        | Returns a hash code value for the object.                                      |
| `notify()`          | Wakes up a single thread waiting on the object's monitor.                      |
| `notifyAll()`       | Wakes up all threads waiting on the object's monitor.                          |
| `toString()`        | Returns a string representation of the object.                                 |
| `wait()`            | Causes the current thread to wait for a `notify()` or `notifyAll()` call.      |

These methods provide foundational behavior to all Java objects and enable critical features like object comparison, threading, and garbage collection.

[back to top](#index)

### **`clone()` Method in Java**

1. **Purpose**:
   - The `clone()` method creates a copy of an object. It performs a **shallow copy** by default and duplicates only the fields of the object, not the referenced objects.

2. **Requirements**:
   - The class must implement the **`Cloneable`** interface (a marker interface).
   - The `clone()` method must be **overridden** in the class.
   - If `Cloneable` is not implemented, `clone()` throws a **`CloneNotSupportedException`**.

3. **Key Characteristics**:
   - **Shallow Copy**: Copies fields of the object, but referenced objects are shared.
   - **Deep Copy**: Must be implemented manually by cloning all referenced objects within the `clone()` method.

4. **Usage**:
   - Use `clone()` when you need to duplicate an object quickly.
   - Avoid using `clone()` for objects with complex relationships unless deep copy is explicitly handled.

5. **Examples**:
   - **Shallow Copy**: Creates a duplicate with shared references to mutable objects.
   - **Deep Copy**: Requires overriding the `clone()` method to clone referenced objects.

6. **Advantages**:
   - Provides a quick and efficient way to copy objects.
   - Reduces repetitive code for copying fields manually.

7. **Disadvantages**:
   - Can lead to shared references (shallow copy), causing unintended side effects.
   - Complex to handle deep copies properly.
   - Alternatives like copy constructors or serialization are often preferred.

8. **Alternatives**:
   - **Copy Constructor**: A constructor that duplicates the object manually.
   - **Serialization/Deserialization**: Serializes the object to a stream and deserializes it for a deep copy.

**When to Use**:
- Use `clone()` for simple objects where shallow copying suffices or performance is critical. For more flexibility and maintainability, consider alternatives like copy constructors or factory methods.

[back to top](#index)

### **Transient Fields in Java**

- **Definition**: Transient fields in Java are not included in the serialized form of an object. They are marked using the `transient` keyword.

- **Purpose**: Used to exclude fields from serialization, typically for:
  - Sensitive data (e.g., passwords).
  - Temporary or derived data.
  - Non-serializable objects.

- **Default Behavior**:
  - During deserialization, transient fields are initialized to their **default values**:
    - `0` for numeric types, `false` for `boolean`, and `null` for objects.

- **Reinitialization**:
  - Transient fields can be reinitialized after deserialization by overriding the `readObject()` method.

- **Example**:
```java
class User implements Serializable {
    String username;
    transient String password; // Excluded from serialization

    User(String username, String password) {
        this.username = username;
        this.password = password;
    }
}
```

**During Serialization**:
- `username` is serialized.
- `password` is ignored and restored as `null` during deserialization. 

**Advantages**:
1. Security: Prevents sensitive data from being serialized.
2. Flexibility: Avoids errors with non-serializable fields.
3. Efficiency: Reduces serialized object size.

[back to top](#index)

### **Serialization/Deserialization in Java (Updated Summary)**

- **Serialization**: Converts an object into a **byte stream** for storage (e.g., file) or transmission (e.g., over a network). Captures the object's state and class metadata.

- **Deserialization**: Reconstructs the object from the **byte stream**, restoring its state.

---

### **Key Points**

1. **Serializable Interface**:
   - The class **must implement the `Serializable` interface** to support serialization.
   - If a referenced object is not serializable, serialization will fail with a `NotSerializableException`.

2. **What is Serialized?**
   - Class metadata (class name, `serialVersionUID`, hierarchy).
   - All **non-transient** and **non-static** fields.
   - References to other objects, provided they are also serializable.

3. **Transient Fields**:
   - Fields marked as `transient` are **not serialized** and are initialized to their **default values** upon deserialization.

4. **Process**:
   - **Serialization**: Use `ObjectOutputStream` to write objects to a file or stream.
   - **Deserialization**: Use `ObjectInputStream` to read objects back into memory.

---

### **Code Example**

**Serialization**:
```java
try (FileOutputStream fos = new FileOutputStream("object.ser");
     ObjectOutputStream oos = new ObjectOutputStream(fos)) {
    oos.writeObject(object); // Serialize the object
}
```

**Deserialization**:
```java
try (FileInputStream fis = new FileInputStream("object.ser");
     ObjectInputStream ois = new ObjectInputStream(fis)) {
    Object obj = ois.readObject(); // Deserialize the object
}
```

---

### **Advantages**:
- Provides easy persistence of object states.
- Handles object graphs (nested references) automatically.
- Enables transmission of objects over a network.

### **Disadvantages**:
- All classes involved must implement `Serializable`.
- Performance overhead due to I/O operations.
- Transient fields and non-serializable objects require additional handling.

---

This mechanism is best suited for simple object storage and transmission scenarios. For more complex use cases, alternatives like JSON or XML serialization (e.g., using libraries like Jackson) are often preferred.

[back to top](#index)


### **Atomic, Volatile, and Synchronized**

---

#### **1. `Atomic`**
- **Purpose**: Provides thread-safe, atomic operations on variables without explicit locking.
- **Key Features**:
  - Guarantees **atomicity** for operations (e.g., increment, compare-and-set).
  - Implicitly ensures **visibility** of updates to all threads.
- **How It Works**:
  - Uses **Compare-And-Swap (CAS)** internally for non-blocking, lock-free updates.
- **Use Cases**:
  - Counters, accumulators, or atomic updates in high-concurrency scenarios.
- **Examples**:
  - `AtomicInteger`, `AtomicLong`, `AtomicReference`.
  
---

#### **2. `Volatile`**
- **Purpose**: Ensures **visibility** of variable updates across threads.
- **Key Features**:
  - Threads always read the latest value of a volatile variable from main memory.
  - Does **not guarantee atomicity** for compound operations (e.g., `count++`).
- **How It Works**:
  - Prevents threads from caching the variable locally.
- **Use Cases**:
  - Simple flags, status variables, or single-read/write scenarios.
- **Example**:
  - A volatile `boolean` flag to stop a thread.

---

#### **3. `Synchronized`**
- **Purpose**: Provides **mutual exclusion** and guarantees both **atomicity** and **visibility**.
- **Key Features**:
  - Ensures only one thread can execute a synchronized block/method at a time.
  - Makes updates visible to other threads after the lock is released.
- **How It Works**:
  - Uses **intrinsic locks (monitor locks)**.
  - Threads attempting to acquire a lock are blocked if another thread holds it.
- **Use Cases**:
  - Protecting critical sections or shared resources in multi-step operations.
- **Example**:
  - A synchronized method to increment a shared counter.

---

### **Comparison**

| **Feature**            | **Atomic**                      | **Volatile**                    | **Synchronized**                 |
|-------------------------|----------------------------------|----------------------------------|----------------------------------|
| **Primary Purpose**     | Atomic operations on variables. | Visibility of variable updates.  | Mutual exclusion and visibility. |
| **Thread-Safety**       | Ensures atomicity and visibility.| Guarantees visibility only.      | Guarantees atomicity and visibility. |
| **Blocking**            | Non-blocking (lock-free).       | Non-blocking.                   | Blocking (threads wait for lock).|
| **Use Cases**           | Counters, accumulators.         | Flags, status indicators.        | Protecting critical sections.    |

---

### **When to Use**
1. **Atomic**: When you need atomicity and performance for simple operations (e.g., counters).
2. **Volatile**: When you only need visibility, not atomicity (e.g., a stop flag).
3. **Synchronized**: When you need both atomicity and visibility for complex, multi-step operations.

[back to top](#index)

### **Object Finalization in Java**

- **Definition**: Finalization is the process where the **`finalize()`** method is called by the **garbage collector** before reclaiming an object's memory.
- **Method**: 
  ```java
  protected void finalize() throws Throwable
  ```
- **Purpose**: Used to perform clean-up tasks like releasing resources (e.g., closing files, freeing memory).

---

### **Key Points**:
1. **When is it Called?**
   - Called by the garbage collector when the object becomes unreachable.
   - No guarantee on the timing or if it will be called at all.

2. **Limitations**:
   - Unpredictable and unreliable.
   - Slows down garbage collection.
   - Called only once per object.

3. **Modern Status**:
   - **Deprecated** as of Java 9 due to inefficiency and better alternatives.

4. **Alternatives**:
   - **`try-with-resources`**: Use for managing files, streams, and other resources.
   - **Explicit Cleanup**: Provide methods like `close()` or `dispose()` for resource management.

---

**Example**:
```java
@Override
protected void finalize() throws Throwable {
    System.out.println("Finalize called for cleanup.");
}
```

**Preferred Alternative**:
```java
try (FileInputStream fis = new FileInputStream("file.txt")) {
    // Process file
} catch (IOException e) {
    e.printStackTrace();
}
``` 

**Summary**: Avoid using `finalize()`; rely on **`try-with-resources`** or manual clean-up methods for resource management.

[back to top](#index)

### **StringBuffer vs StringBuilder**

`StringBuffer` and `StringBuilder` are classes in Java used to manipulate strings dynamically. Both are mutable, meaning their content can be modified without creating a new object. However, they differ primarily in terms of **thread safety** and **performance**.

---

### **Key Differences**

| **Feature**              | **StringBuffer**                                       | **StringBuilder**                                   |
|--------------------------|-------------------------------------------------------|---------------------------------------------------|
| **Thread Safety**         | Thread-safe: Methods are synchronized.               | Not thread-safe: No synchronization.             |
| **Performance**           | Slower due to synchronization overhead.              | Faster as it doesn’t synchronize methods.        |
| **Usage in Multithreading**| Suitable for multi-threaded environments.            | Suitable for single-threaded environments.       |
| **Introduced In**         | Java 1.0                                             | Java 5                                           |

---

### **Similarities**
1. **Mutability**:
   - Both classes allow modification of strings (e.g., append, insert, delete) without creating new objects.
   
2. **Methods**:
   - Both share similar methods like `append()`, `insert()`, `delete()`, `reverse()`, etc.

3. **Underlying Mechanism**:
   - Both use a **mutable character array** internally.

---

### **Example: StringBuffer**
```java
public class StringBufferExample {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer("Hello");
        sb.append(" World"); // Thread-safe modification
        System.out.println(sb); // Output: Hello World
    }
}
```

### **Example: StringBuilder**
```java
public class StringBuilderExample {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("Hello");
        sb.append(" World"); // Faster but not thread-safe
        System.out.println(sb); // Output: Hello World
    }
}
```

---

### **When to Use**
1. **Use `StringBuffer`**:
   - In multi-threaded applications where multiple threads modify the same string object.
   - Example: Logging systems in a concurrent environment.

2. **Use `StringBuilder`**:
   - In single-threaded applications or when thread safety is not required.
   - Example: String manipulations in performance-critical tasks.

---

### **Summary**
- **StringBuffer**: Thread-safe but slower due to synchronization.
- **StringBuilder**: Faster but not thread-safe. Preferable in single-threaded scenarios.

[back to top](#index)

### Comparison of some **similar data structures** in Java based on functionality, thread-safety, performance, and usage:

---

### **1. `ArrayList` vs `LinkedList`**
| **Feature**          | **ArrayList**                             | **LinkedList**                            |
|-----------------------|-------------------------------------------|-------------------------------------------|
| **Underlying Data Structure** | Dynamic array                          | Doubly linked list                        |
| **Access Time**       | Fast (`O(1)` for index-based access)      | Slow (`O(n)` for index-based access)      |
| **Insertion/Deletion**| Slow (`O(n)` for shifting elements)       | Fast (`O(1)` at the beginning/end)        |
| **Memory Usage**      | Less memory (stores only data).           | More memory (stores data and pointers).   |
| **Thread Safety**     | Not thread-safe.                         | Not thread-safe.                          |
| **Use Case**          | Random access of elements.               | Frequent insertions and deletions.        |

---

### **2. `HashMap` vs `Hashtable`**
| **Feature**           | **HashMap**                              | **Hashtable**                             |
|-----------------------|-------------------------------------------|-------------------------------------------|
| **Thread Safety**     | Not thread-safe.                         | Thread-safe (synchronized methods).       |
| **Null Keys/Values**  | Allows one `null` key and multiple `null` values. | Does not allow `null` keys or values.     |
| **Performance**       | Faster (no synchronization overhead).    | Slower due to synchronization.            |
| **Introduced In**     | Java 1.2                                 | Java 1.0                                  |
| **Use Case**          | Non-concurrent, high-performance scenarios. | Concurrent access in legacy systems.      |

---

### **3. `HashMap` vs `ConcurrentHashMap`**
| **Feature**           | **HashMap**                              | **ConcurrentHashMap**                     |
|-----------------------|-------------------------------------------|-------------------------------------------|
| **Thread Safety**     | Not thread-safe.                         | Thread-safe (uses segment locking).       |
| **Concurrency Level** | No support for concurrency.              | Allows multiple threads to read/write simultaneously. |
| **Null Keys/Values**  | Allows one `null` key and multiple `null` values. | Does not allow `null` keys or values.     |
| **Performance**       | Faster in single-threaded environments.  | Faster in multi-threaded environments.    |
| **Use Case**          | Single-threaded applications.            | Concurrent, thread-safe access to maps.   |

---

### **4. `Vector` vs `ArrayList`**
| **Feature**           | **Vector**                               | **ArrayList**                             |
|-----------------------|-------------------------------------------|-------------------------------------------|
| **Thread Safety**     | Thread-safe (synchronized methods).       | Not thread-safe.                          |
| **Performance**       | Slower due to synchronization overhead.   | Faster in non-threaded environments.      |
| **Growth Mechanism**  | Doubles its size when needed.             | Increases by 50% when needed.             |
| **Legacy/Modern**     | Legacy class (Java 1.0).                 | Modern class (Java 1.2, part of `Collection` framework). |
| **Use Case**          | Multi-threaded environments (legacy systems). | Single-threaded environments.            |

---

### **5. `HashSet` vs `TreeSet` vs `LinkedHashSet`**
| **Feature**           | **HashSet**                              | **TreeSet**                               | **LinkedHashSet**                         |
|-----------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| **Underlying Data Structure** | Hash table.                          | Red-Black tree.                           | Hash table + Linked list.                 |
| **Ordering**          | No guaranteed order.                     | Sorted order (natural or comparator-defined). | Insertion order is maintained.           |
| **Null Elements**     | Allows one `null` element.               | Does not allow `null` elements.           | Allows one `null` element.               |
| **Performance**       | Fast (`O(1)` for add, remove, contains).  | Slower (`O(log n)` for add, remove, contains). | Moderate (`O(1)` with insertion order). |
| **Use Case**          | High-performance lookups.                | Sorted data requirements.                 | Preserving insertion order.               |

---

### **6. `Stack` vs `Deque`**
| **Feature**           | **Stack**                                | **Deque**                                 |
|-----------------------|-------------------------------------------|-------------------------------------------|
| **Thread Safety**     | Thread-safe (legacy, synchronized methods).| Not thread-safe (unless `ConcurrentLinkedDeque` is used). |
| **Performance**       | Slower due to synchronization.           | Faster in non-threaded environments.      |
| **Flexibility**       | LIFO (Last-In-First-Out) operations only. | Supports both LIFO and FIFO (First-In-First-Out). |
| **Modern Equivalent** | Legacy class.                            | Preferred for stack and queue operations. |
| **Use Case**          | Use in legacy codebases.                 | Use in modern applications.               |

---

### **7. `TreeMap` vs `HashMap`**
| **Feature**           | **HashMap**                              | **TreeMap**                               |
|-----------------------|-------------------------------------------|-------------------------------------------|
| **Ordering**          | No specific order.                       | Sorted order (natural or comparator-defined). |
| **Null Keys**         | Allows one `null` key.                   | Does not allow `null` keys.               |
| **Performance**       | Fast (`O(1)` for get/put).               | Slower (`O(log n)` for get/put).          |
| **Use Case**          | High-performance key-value storage.      | Sorted key-value storage.                 |

---

### **8. `PriorityQueue` vs `Deque`**
| **Feature**           | **PriorityQueue**                        | **Deque**                                 |
|-----------------------|-------------------------------------------|-------------------------------------------|
| **Purpose**           | Retrieves elements based on priority.    | Double-ended operations (add/remove from both ends). |
| **Ordering**          | Maintains a natural or comparator-defined order. | No specific order.                       |
| **Null Elements**     | Does not allow `null` elements.           | Allows `null` elements.                  |
| **Use Case**          | Scheduling tasks by priority.            | Stacks or queues with flexible operations.|

---

### **Summary**
- Choose based on requirements like **thread safety** (e.g., `Vector` vs `ArrayList`), **ordering** (e.g., `TreeSet` vs `HashSet`), and **performance** (e.g., `HashMap` vs `TreeMap`).
- Modern data structures (`ArrayList`, `Deque`, `ConcurrentHashMap`) are preferred over legacy ones (`Vector`, `Hashtable`, `Stack`).