## Table of Contents
- [Hibernate](#hibernate)
- [Java Persistent API (JPA)](#java-persistence-api-jpa)
- [Example of creating DAO layer `Repository interface` using hibernate using JPQL.](#example-of-creating-dao-layer-repository-interface-using-hibernate-using-jpql)
- [Complex Queries in Hibernate: Two Choices - JPQL vs. Criteria Builder](#complex-queries-in-hibernate-two-choices---jpql-vs-criteria-builder)


@Entity
@Table(name="mystudents")
@Id

### **Hibernate**  
Hibernate is an **Object-Relational Mapping (ORM)** framework for Java that maps Java objects to relational database tables. It simplifies database operations by eliminating complex SQL queries, offering features like caching, automatic schema generation, and HQL (Hibernate Query Language).

<sub>[back to top](#table-of-contents)</sub>

---

### **Java Persistence API (JPA)**  
JPA is a **specification** for ORM in Java. It defines how Java objects interact with database tables but doesn't provide implementation. Frameworks like **Hibernate** implement JPA.

---

### **Key Differences**  
| **Aspect**         | **Hibernate**                         | **JPA**                                |
|--------------------|----------------------------------------|----------------------------------------|
| **Type**           | Framework                             | Specification                          |
| **Usage**          | Works standalone or with JPA          | Requires an implementation like Hibernate |
| **Query Language** | HQL (Hibernate Query Language)        | JPQL (Java Persistence Query Language) |

---

### **Summary**  
- Use **JPA** for standardization.  
- Use **Hibernate** when you need advanced features or flexibility.  
Hibernate can be a JPA provider.

<sub>[back to top](#table-of-contents)</sub>

---

## Example of creating DAO layer `Repository interface` using hibernate using JPQL.
- Extends JPARepository interface 
- Custom Query 

```java
package com.sunny.java.hibernate.trial.repository;

import com.sunny.java.hibernate.trial.repository.model.Musician;
import com.sunny.java.hibernate.trial.repository.model.Band;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface MusicianRepository extends JpaRepository<Musician, Long> {

    @Query("select b from Band b join b.musicians m where m.id = ?1")
    List<Band> findAllBandsByMusicianId(long musicianId);

}
```

<sub>[back to top](#table-of-contents)</sub>

---

## **Complex Queries in Hibernate: Two Choices - JPQL vs. Criteria Builder**



### **1. Complex Insertions**

For complex insertions, you can use **JPQL** or **EntityManager**.

#### **Using JPQL for Queries (Not Insertions)**
- **JPQL** is used for querying entities, not insertions. You can execute `SELECT`, `UPDATE`, and `DELETE` operations with JPQL, but **insertions** must be handled by `EntityManager` using the `persist()` method.
  
- Example **JPQL** query for retrieving employees with a salary above a certain threshold:
  ```java
  @Query("SELECT e FROM Employee e WHERE e.salary > :salary")
  List<Employee> findEmployeesWithHighSalary(@Param("salary") double salary);
  ```

#### **Using EntityManager for Insertion**
- For insertions, we use **`EntityManager`** to persist entities, not JPQL.
- Example using **`EntityManager`** for insertion:
  ```java
  @Transactional
  public void insertEmployee(String name, String department) {
      Employee employee = new Employee(name, department);
      entityManager.persist(employee);
  }
  ```

**Where `EntityManager` is used:**
- `EntityManager` is used to persist entities for **insertions**, handling the lifecycle of entities and their interaction with the database.

---

### **2. Complex Queries**

You can perform complex queries using **JPQL** or **Criteria Builder** depending on your needs.

#### **Using JPQL for Complex Queries**
- **JPQL** is great for predefined, readable queries that are known at compile time.
- Example for a **complex query** to fetch employees with salaries above a threshold, sorted by department:
  ```java
  @Query("SELECT e FROM Employee e JOIN e.department d WHERE e.salary > :salary ORDER BY d.name")
  List<Employee> findEmployeesWithHighSalary(@Param("salary") double salary);
  ```

#### **Using Criteria Builder for Complex Queries**
- **Criteria Builder** is ideal for dynamic queries where the structure or parameters might change at runtime.
- Example of the same **complex query** using **Criteria Builder**:
  ```java
  CriteriaBuilder cb = entityManager.getCriteriaBuilder();
  CriteriaQuery<Employee> cq = cb.createQuery(Employee.class);
  Root<Employee> employee = cq.from(Employee.class);
  Join<Employee, Department> department = employee.join("department");

  cq.select(employee)
    .where(cb.greaterThan(employee.get("salary"), salary))
    .orderBy(cb.asc(department.get("name")));

  List<Employee> result = entityManager.createQuery(cq).getResultList();
  ```

**Where `EntityManager` is used:**
- `EntityManager` is used to execute **both JPQL** and **Criteria Builder** queries, providing control over query execution and entity management.

---

### **What is `EntityManager`?**
- **`EntityManager`** is a JPA interface that provides methods to manage entities in the persistence context. It handles **CRUD operations**, executes **queries (JPQL/Criteria)**, and manages the state of entities.
  
- **Key Responsibilities:**
  - **Persistence Operations:** Methods like `persist()`, `merge()`, and `remove()`.
  - **Query Execution:** Executes **JPQL** or **native SQL** queries using `createQuery()`.
  - **Transaction Management:** Ensures data consistency within a transaction.
  - **Entity State Management:** Tracks entities as **managed**, **detached**, or **removed**.

---

### **Choosing Between JPQL and Criteria Builder**
- **JPQL:** Ideal for static, readable queries where the structure and parameters are known at compile time.
- **Criteria Builder:** Ideal for dynamic, type-safe queries that are built programmatically at runtime.

---

### **Summary**
- **Insertions:** 
  - Use **EntityManager** and **persist()** for insertions.
- **Queries:** 
  - **JPQL** is great for simple, predefined queries.
  - **Criteria Builder** is preferred for dynamic, programmatically created queries.


<sub>[back to top](#table-of-contents)</sub>
