## Table of Contents
- [Key Points](#key-points)
- [Spring Boot Library Management System that uses `Redis for caching` and `PostgreSQL as the database`](#spring-boot-library-management-system-that-uses-redis-for-caching-and-postgresql-as-the-database)
- [Redis Template](#redis-template)


### Key points:
- `spring-boot-starter-data-redis` & `spring-boot-starter-cache` dependency
- Redis Config
```
# Redis configuration
spring.redis.host=localhost
spring.redis.port=6379
spring.redis.password=yourpassword
spring.redis.ssl=false

```
- @EnableCaching in main Class
- @Cachable & @CacheEvit Method in Service
```java
    // Cache the result of getting a book by ID
    @Cacheable(value = "book", key = "#id")
    public Book getBookById(Long id) {
        return bookRepository.findById(id).orElse(null);
    }

    // Evict the cache for a specific book when it is saved
    @CacheEvict(value = "book", key = "#book.id")
    public Book saveBook(Book book) {
        return bookRepository.save(book);
    }

    // Evict cache for all books
    @CacheEvict(value = "books", allEntries = true)
    public void deleteAllBooks() {
        bookRepository.deleteAll();
    }
```
- For finer control on Redis we can use `RedisService` class which has `RedisTemplate` dependency object.

---
## **Spring Boot Library Management System** that uses **Redis for caching** and **PostgreSQL as the database**.

### Prerequisites:
1. **PostgreSQL** database running and accessible.
2. **Redis** server running for caching.

### Step-by-Step Implementation

### 1. **Add Dependencies in `pom.xml`**
Add the necessary dependencies for **Spring Boot**, **PostgreSQL**, **Redis**, and **Spring Data JPA**.

```xml
<dependencies>
    <!-- Spring Boot Starter Web -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <!-- Spring Boot Starter Data JPA for PostgreSQL -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>

    <!-- PostgreSQL JDBC Driver -->
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
    </dependency>

    <!-- Spring Boot Starter Data Redis -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-redis</artifactId>
    </dependency>

    <!-- Spring Boot Starter Cache for Redis -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-cache</artifactId>
    </dependency>

    <!-- Lettuce Redis client -->
    <dependency>
        <groupId>io.lettuce.core</groupId>
        <artifactId>lettuce-core</artifactId>
    </dependency>
</dependencies>
```

### 2. **Configure `application.properties`**
Define the connection details for **PostgreSQL** and **Redis** in `src/main/resources/application.properties`.

```properties
# PostgreSQL configuration
spring.datasource.url=jdbc:postgresql://localhost:5432/librarydb
spring.datasource.username=postgres
spring.datasource.password=yourpassword
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true

# Redis configuration
spring.redis.host=localhost
spring.redis.port=6379
spring.redis.password=yourpassword
spring.redis.ssl=false

# Enable caching
spring.cache.type=redis
```

### 3. **Define the Entity Class (`Book.java`)**
Create an entity class `Book` that represents a book in the library.

```java
package com.library.model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;

@Entity
public class Book {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    private String author;
    private String genre;

    // Getters and Setters
}
```

### 4. **Create the Repository (`BookRepository.java`)**
Define the `BookRepository` interface extending `JpaRepository` to interact with the PostgreSQL database.

```java
package com.library.repository;

import com.library.model.Book;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BookRepository extends JpaRepository<Book, Long> {
}
```

### 5. **Enable Caching in `LibraryApplication.java`**
Add `@EnableCaching` to enable caching in the application.

```java
package com.library;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;

@SpringBootApplication
@EnableCaching
public class LibraryApplication {
    public static void main(String[] args) {
        SpringApplication.run(LibraryApplication.class, args);
    }
}
```

### 6. **Define the Service Layer with Caching (`BookService.java`)**
In the service layer, use Redis for caching. You can cache the list of books or a single book by ID.

```java
package com.library.service;

import com.library.model.Book;
import com.library.repository.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookService {

    @Autowired
    private BookRepository bookRepository;

    // Cache the result of getting all books
    @Cacheable(value = "books", key = "'allBooks'")
    public List<Book> getAllBooks() {
        return bookRepository.findAll();
    }

    // Cache the result of getting a book by ID
    @Cacheable(value = "book", key = "#id")
    public Book getBookById(Long id) {
        return bookRepository.findById(id).orElse(null);
    }

    // Evict the cache for a specific book when it is saved
    @CacheEvict(value = "book", key = "#book.id")
    public Book saveBook(Book book) {
        return bookRepository.save(book);
    }

    // Evict cache for all books
    @CacheEvict(value = "books", allEntries = true)
    public void deleteAllBooks() {
        bookRepository.deleteAll();
    }
}
```

### 7. **Create the Controller (`BookController.java`)**
Define a controller to handle HTTP requests.

```java
package com.library.controller;

import com.library.model.Book;
import com.library.service.BookService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/books")
public class BookController {

    @Autowired
    private BookService bookService;

    @GetMapping("/")
    public List<Book> getBooks() {
        return bookService.getAllBooks();
    }

    @GetMapping("/{id}")
    public Book getBook(@PathVariable Long id) {
        return bookService.getBookById(id);
    }

    @PostMapping("/")
    public Book saveBook(@RequestBody Book book) {
        return bookService.saveBook(book);
    }

    @DeleteMapping("/")
    public void deleteAllBooks() {
        bookService.deleteAllBooks();
    }
}
```

### 8. **Run the Application**
Run the Spring Boot application:

```bash
mvn spring-boot:run
```

### 9. **PostgreSQL Setup**
Make sure the **PostgreSQL** database is set up:

```sql
CREATE DATABASE librarydb;
```

### 10. **Test the Application**

- Add a book using the `POST /books/` endpoint.
- Get all books using the `GET /books/` endpoint. The result will be cached in Redis.
- Get a specific book by ID using the `GET /books/{id}` endpoint. This will also use Redis caching.

### Redis Cache Behavior:
- The first time you fetch all books (`GET /books/`), it will hit the PostgreSQL database and cache the results in Redis.
- When you fetch a book by ID (`GET /books/{id}`), it will first check the Redis cache. If the book is not in the cache, it will query the database and store the result in Redis for future requests.

### Conclusion:
This example shows how to integrate **PostgreSQL** for storing data and **Redis** for caching in a **Spring Boot application**. Caching can help reduce the load on the database and improve performance when querying frequently accessed data.


## Redis Template
The `RedisTemplate` is a central component in Spring Data Redis, used to interact with Redis. It provides a high-level abstraction for performing Redis operations, such as storing and retrieving objects, handling various Redis data structures, and performing transactions. Here's why we use `RedisTemplate`:

### Key Reasons to Use `RedisTemplate`:
1. **Simplifies Redis Operations**: It abstracts away the low-level Redis commands and provides a more user-friendly interface for interacting with Redis, like `opsForValue()`, `opsForList()`, `opsForHash()`, etc.
  
2. **Serialization and Deserialization**: It automatically handles serialization and deserialization of data. It supports different serializers like `StringRedisSerializer`, `Jackson2JsonRedisSerializer`, etc., making it easier to store and retrieve complex objects.

3. **Supports Redis Data Structures**: It provides support for Redis data types such as strings, lists, sets, hashes, and sorted sets, making it versatile for various use cases.

4. **Transactional Operations**: It supports Redis transactions, enabling you to execute multiple Redis commands in a single transaction.

5. **Integration with Spring Caching**: `RedisTemplate` is used under the hood when Spring's caching mechanism is configured to use Redis. It provides a way to store and retrieve cached data.

### Example of Using `RedisTemplate`:
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

@Service
public class RedisService {

    @Autowired
    private RedisTemplate<String, Object> redisTemplate;

    // Save a key-value pair in Redis
    public void saveValue(String key, Object value) {
        redisTemplate.opsForValue().set(key, value);
    }

    // Get a value from Redis by its key
    public Object getValue(String key) {
        return redisTemplate.opsForValue().get(key);
    }

    // Delete a value by its key
    public void deleteValue(String key) {
        redisTemplate.delete(key);
    }
}
```

In this example:
- `redisTemplate.opsForValue()` is used to store and retrieve a simple key-value pair in Redis.
- It simplifies the interactions with Redis, abstracts away the complexity of using the low-level Redis API, and provides a higher-level, cleaner approach to handling Redis operations.