## Table of Contents
- [What is Spring boot?](#what-is-spring-boot)
- [For Accessing Properties in `application.properties` File](#for-accessing-properties-in-applicationproperties-file)
- [Annotations in Spring Boot](#annotations-in-spring-boot)
- [Creating a bean in Spring Boot](#creating-a-bean-in-spring-boot)
- [What are the different autowiring modes?](#what-are-the-different-autowiring-modes)
- [What are the different bean scopes in Spring?](#what-are-the-different-bean-scopes-in-spring)
- [Database Configuration](#database-configuration)
- [Different ways to exclude dependencies in Spring Boot.](#different-ways-to-exclude-dependencies-in-spring-boot)
- [Datasource](#datasource)
- [JdbcTemplate](#jdbctemplate)
- [Different datasources we can use in Spring.](#different-datasource-we-can-use-in-spring)
- [Dependency Injection](#dependency-injection)
- [Inversion of control](#inversion-of-control)
- [How to Secure Spring Application?](#how-to-secure-spring-application)
- [How Spring Boot works internally](#how-spring-boot-works-internally)
- [Spring Boot Core Module](#spring-boot-core-module)
- [How Does the Dispatcher Servlet work in Spring boot](#how-does-the-dispatcherservlet-work-in-spring-boot)  
- [What is spring boot actuator?](#what-is-spring-boot-actuator)
- [What are some commonly used endpoints in spring boot](#what-are-some-commonly-used-endpoints-in-spring-boot-actuator)
- [Changing Property at runtime](#changing-property-at-runtime)
- [Aspect Oriented Programming (AOP)](#aspect-oriented-programming-aop)
- [@ControllerAdvice](#controlleradvice)
- [Stream Vs for loop](#stream-vs-for-loop)

@EnableScheduling, @Scheduled(cron)
### What is Spring boot?
- auto-configurationa and set-up process.
- rapid application development.
- provides embedded server.

<sub>[back to top](#table-of-contents)</sub>

### For Accessing Properties in `application.properties` File

1. **Using `@Value` Annotation**  
   Injects the value of a property directly into a field, method, or constructor.

   ```java
   @Value("${spring.datasource.url}")
   private String datasourceUrl;
   ```

   - **Example**: Access `spring.datasource.url` from `application.properties`.

2. **Using `@ConfigurationProperties`**  
   Maps a group of related properties to a POJO.

   ```java
   @Component
   @ConfigurationProperties(prefix = "spring.datasource")
   public class DataSourceConfig {
       private String url;
       private String username;
       private String password;
       // Getters and Setters
   }
   ```

   - **Example**: Maps all properties under `spring.datasource` (like `spring.datasource.url`, `username`, `password`).

3. **Using `Environment` Interface**  
   Access properties programmatically.

   ```java
   @Autowired
   private Environment env;

   public void getProperty() {
       String url = env.getProperty("spring.datasource.url");
   }
   ```

   - **Example**: Retrieve properties using keys.

#### Best Practice:  
- Use `@ConfigurationProperties` for structured and reusable configurations.

<sub>[back to top](#table-of-contents)</sub>
### **Annotations in Spring Boot**

1. **`@SpringBootApplication`**  
   - Combines `@Configuration`, `@EnableAutoConfiguration`, and `@ComponentScan` for setting up Spring Boot applications.

2. **`@Configuration`**  
   - Marks a class as a source of bean definitions.

3. **`@EnableAutoConfiguration`**  
   - Enables Spring Boot to auto-configure beans based on the dependencies in the classpath.

4. **`@ComponentScan`**  
   - Scans the specified package(s) for components (`@Component`, `@Service`, `@Repository`, etc.).

5. **`@Autowired`**  
   - Automatically injects dependencies into a bean.

6. **`@Component`**  
   - Marks a class as a generic Spring-managed component.

7. **`@Service`**  
   - Marks a class as a service layer component for business logic.

8. **`@Repository`**  
   - Marks a class as a data access layer component, also enabling exception translation.

9. **`@Qualifier`**  
   - Specifies the bean to inject when multiple candidates are available.

10. **`@ResponseBody`**  
    - Converts the return value of a method to JSON or XML and writes it directly to the HTTP response body.

11. **`@RestController`**  
    - Combines `@Controller` and `@ResponseBody` to handle RESTful web requests.

12. **`@ApplicationContext`**  
    - Not an annotation. Refers to the Spring container that manages beans and configurations.

<sub>[back to top](#table-of-contents)</sub>

### **Creating a Bean in Spring Boot**

Beans in Spring Boot can be created using several approaches, including annotations, XML configuration, or manual definitions in configuration classes. Here’s an overview:

---

#### **1. Using `@Component` Annotation**
- Annotate the class with `@Component` to mark it as a Spring Bean.
- Spring automatically detects it during component scanning.

```java
@Component
public class MyService {
    // Bean definition
}
```

**Component Scanning**  
To enable component scanning, use `@ComponentScan` with the package name containing the beans:

```java
@ComponentScan("beans.container")
```

---

#### **2. Using `@Bean` Annotation in a Configuration Class**
- Define a method annotated with `@Bean` in a class marked with `@Configuration`.  
- The method returns an instance of the Bean.

```java
@Configuration
public class MyConfiguration {
    @Bean
    public Network network() {
        return new Network();
    }
}
```

---

#### **3. Using XML Configuration**
- Define beans in an XML file (e.g., `resources/config.xml`) with constructor and setter injections.

#### Example: Constructor Injection
```xml
<bean name="network" class="com.interview.beans.Network">
    <constructor-arg value="12"/> <!-- Constructor injection -->
    <constructor-arg value="12.1"/> <!-- Constructor injection -->
</bean>
```

#### Example: Setter Injection
```xml
<bean name="network" class="com.interview.beans.Network">
    <property name="network" ref="network"/> <!-- Setter injection -->
</bean>
```

#### Example: Autowiring
- Use `autowire="byName"` or `autowire="byType"` for automatic dependency injection without explicitly writing `<property>` tags.

```xml
<bean name="network" class="com.interview.beans.Network" autowire="byName"/>
```

---

#### **4. When to Choose Each Approach**
- **`@Component`/`@ComponentScan`**: Use for straightforward, auto-detected Bean creation in typical applications.
- **`@Bean` Annotation**: Use for manual and fine-grained control over Bean instantiation, especially when creating third-party class instances.
- **XML Configuration**: Legacy or specific use cases where XML configuration is required.

#### **Key Notes**
- Spring Boot prefers annotation-based configurations over XML for simplicity and modern development practices. 
- Use XML configurations only when working with older Spring versions or integrating with legacy systems.

<sub>[back to top](#table-of-contents)</sub>

### What are the different Autowiring modes?
- no  
- byName  
- byType  
- constructor  

<sub>[back to top](#table-of-contents)</sub>

### What are the different bean scopes in spring?
-   Singleton
-   Prototype
-   Request
-   Session
-   Globalsession

<sub>[back to top](#table-of-contents)</sub>

### Database Configuration.
For setting database connection we need to set the values of url, username and password for database in application.properties file.

`application.properties`
```properties
spring.datasource.url = jdbc:mysql://localhost:3306/boot_work
sprig.datasource.username=root
spring.datasource.password=root 
```
### Note:
For using different datasource other than default HikariCP. We need to exclude the datasource and jdbcTempalte dependencies.

<sub>[back to top](#table-of-contents)</sub>

### Different ways to exclude dependencies in spring boot.
#### Example:  
#### `1. Using excludeName Attribute`
```java
@SpringBootApplication(excludeName = {"org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration"})
public class MySpringBootApplication {
    public static void main(String[] args) {
        SpringApplication.run(MySpringBootApplication.class, args);
    }
}
```
#### `2. Exclude Dependency in Maven`
```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-web</artifactId>
    <version>5.3.29</version>
    <exclusions>
        <exclusion>
            <groupId>commons-logging</groupId>
            <artifactId>commons-logging</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

#### `3. Exclude Dependency in Gradle`
```groovy
dependencies {
    implementation('org.springframework:spring-web:5.3.29') {
        exclude group: 'commons-logging', module: 'commons-logging'
    }
}
```

<sub>[back to top](#table-of-contents)</sub>

### DataSource
A DataSource is an abstraction that provides a way to manage a database connection pool and handles acquiring connections for querying or updating the database.

<sub>[back to top](#table-of-contents)</sub>

### JdbcTemplate

JdbcTemplate is a class in Spring Framework that simplifies interaction with a relational database using JDBC (Java Database Connectivity). It abstracts and handles the repetitive tasks of connecting to the database, executing SQL queries, and processing results.

<sub>[back to top](#table-of-contents)</sub>

### Different Datasource we can use in Spring.
- c3p0
- HikariCP
- Apache DBCP
- Tomcat JDBC Connection Pooling
- DriverManagerDataSource

#### Example:
```java
@Configuration
public class DataConfig {
    
    //@Value is used for accessing the value of properties present in application.properties file.
    @Value("${spring.datasource.url}")
    private String url;

    @Value("${spring.datasource.username}")
    private String username;
    
    @Value("${spring.datasource.password}")
    private String password;
    
    @Bean
    public DataSource dataSource() {
        ComboPooledDataSource datasource = new ComboPooledDataSource();
        datasource.setJdbcUrl(url);
        datasource.setUser(username);  // Corrected variable name here
        datasource.setPassword(password);
        return datasource;  // Corrected return variable name
    }

    @Bean
    public JdbcTemplate jdbcTemplate() {
        return new JdbcTemplate(dataSource());  // Added missing semicolon
    }
}
```

<sub>[back to top](#table-of-contents)</sub>

### Dependency Injection
Dependency Injection is a technique where an object’s dependencies are provided (injected) by an external system, like the Spring Framework, rather than the object creating the dependencies itself.

#### Why use it?

To make the code loosely coupled, testable, and easier to maintain.
Types of Dependency Injection:

Constructor Injection: Dependencies are passed through the class constructor.  
Setter Injection: Dependencies are set via setter methods.

#### Analogy
Think of it like ordering food at a restaurant:

You don’t go into the kitchen (your class) and make your own meal (create the dependency).
Instead, the waiter (Spring) delivers the meal (dependency) to your table (class).

<sub>[back to top](#table-of-contents)</sub>

### Inversion of Control

Inversion of Control (IoC) is a design principle in which the control of object creation and dependency management is inverted from the application code to an external framework or container.

#### Analogy
Imagine you're hosting a party:

Without IoC: You handle everything—buying groceries, cooking, serving food, and cleaning up.
With IoC: You hire a catering service (the framework). The caterers take over all the tasks, and you just enjoy the party.


### How to Secure Spring Application?

Securing a Spring application involves implementing various layers of protection to safeguard against unauthorized access, data breaches, and other vulnerabilities. Here’s a comprehensive approach to securing your Spring application:

---

### **1. Secure Application Properties**
- **Use Encrypted Credentials:**
  - Avoid hardcoding sensitive data (e.g., database credentials, API keys).
  - Use Spring’s support for encrypted properties with tools like [Jasypt](https://github.com/ulisesbocchio/jasypt-spring-boot).
- **Environment Variables:**
  - Store sensitive information like database passwords in environment variables or externalized configuration.

---

### **2. Enable HTTPS**
- Use HTTPS to encrypt data in transit:
  - Configure Spring Boot to use SSL by adding a keystore to your application:
    ```properties
    server.port=8443
    server.ssl.key-store=classpath:keystore.p12
    server.ssl.key-store-password=yourpassword
    server.ssl.key-store-type=PKCS12
  - Generate a keystore using tools like `keytool` or obtain an SSL certificate from a trusted provider.
    
---

### **3. Secure Spring Security Configuration**
- Use Spring Security for Authentication and Authorization:
  ```java
  @Configuration
  @EnableWebSecurity
  public class SecurityConfig extends WebSecurityConfigurerAdapter {
      @Override
      protected void configure(HttpSecurity http) throws Exception {
          http
              .authorizeRequests()
              .antMatchers("/admin/**").hasRole("ADMIN")
              .antMatchers("/user/**").hasRole("USER")
              .antMatchers("/", "/public/**").permitAll()
              .and()
              .formLogin()
              .and()
              .csrf().disable();  // Enable if using stateful sessions
      }
  }
  ```

- **Use Password Encoding:**
  - Use `BCryptPasswordEncoder` to hash passwords:
    ```java
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
    ```

---

### **4. Validate User Inputs**
- Use validation frameworks like Hibernate Validator for data validation.
  ```java
  @NotNull
  @Size(min = 8, max = 20)
  private String username;
  ```
- Sanitize inputs to avoid SQL Injection and XSS attacks.
- If using query parameters, use parameterized queries or Spring Data JPA.

---

### **5. Secure APIs**
- **OAuth2/OpenID Connect:**
  - Use Spring Security OAuth2 for token-based authentication.
  - Protect your APIs with JWT (JSON Web Tokens):
    ```properties
    spring.security.oauth2.resourceserver.jwt.issuer-uri=https://your-issuer
    ```

- **Rate Limiting:**
  - Prevent abuse by implementing rate limiting using libraries like Bucket4j or Resilience4j.

---

### **6. Prevent CSRF (Cross-Site Request Forgery)**
- Enable CSRF protection for stateful applications.
- For stateless applications (APIs), use secure headers like `X-CSRF-TOKEN` or `Authorization` tokens.

---

### **7. Secure Headers**
- Add HTTP security headers to prevent attacks:
  ```java
  @Bean
  public WebSecurityConfigurerAdapter securityHeaders() {
      return new WebSecurityConfigurerAdapter() {
          @Override
          protected void configure(HttpSecurity http) throws Exception {
              http.headers()
                  .contentSecurityPolicy("script-src 'self'")
                  .and()
                  .xssProtection()
                  .and()
                  .frameOptions().deny();
          }
      };
  }
  ```

---

### **8. Monitor and Log**
- Use monitoring tools like **Spring Boot Actuator** to track application health.
- Use logging frameworks like Logback and ensure logs don’t expose sensitive information.
- Integrate with centralized logging and monitoring solutions (e.g., ELK Stack, Prometheus).

---

### **9. Secure Dependency Management**
- Keep dependencies up to date to avoid vulnerabilities.
- Use tools like **OWASP Dependency-Check** or **Snyk** to scan for vulnerabilities in libraries.

---

### **10. Implement Database Security**
- Use parameterized queries or ORM frameworks like JPA to prevent SQL injection.
- Use least-privilege access for database users.

---

### **11. Protect Against Common Vulnerabilities**
- **Injection Attacks:** Use prepared statements or Hibernate.
- **XSS:** Sanitize outputs using libraries like OWASP Java HTML Sanitizer.
- **Session Hijacking:** Use secure cookies (`Secure` and `HttpOnly` flags) and session timeouts.

---

### **12. Use a Web Application Firewall (WAF)**
- Deploy a WAF to protect your application from external threats.

---

### **13. Secure Deployment**
- Deploy applications in secure environments:
  - Use containerization tools like Docker with properly configured images.
  - Use orchestration tools like Kubernetes for managing clusters securely.

---

By implementing these practices, you can significantly enhance the security of your Spring application. 

<sub>[back to top](#table-of-contents)</sub>


## [How spring boot works internally](https://www.youtube.com/watch?v=qlygg_H1M20)

Starter POM

Inside Maven dependencies we have JAR Files.
Inside the jar files. We have Folder name as `META_INF/spring.factories`

- Enable
- Disable

Based on @Conditional and @Configuration

### Why we need main method in SpringBoot
• Main method is not required for the typical deployment scenario of building a war and placing it in webapps folder  
• However, if you want to be able to launch the application from within an IDE (e.g. with Eclipse's Run As -> Java Application) while developing or build an executable jar or a war that can run standalone with Spring Boot's embedded tomcat by just java -jar
myapp.war command.

### SpringApplication.run(...);  
Following is the high level flow of how spring boot works.

From the run method, the main application context is kicked off which in turn searches for the classes annotated with @configuration, initializes all the declared beans in those configuration classes, and stores those beans in JVM, specifically in a space inside JVM which is known as IOC container. After creation of all the beans, automatically configures the dispatcher servlet and registers the default handler mappings, messageconverts and all other basic things.

run(...) Internal Flow
- Create Application Context
- Check Application Type
- Register the annotated class beans with the context
- Creates an instance of TomcatEmbeddedServletContainer and adds the context

<sub>[back to top](#table-of-contents)</sub>

## Spring Boot Core Module

The **Spring Framework** is organized into several modules that provide various functionalities, each addressing a specific concern in application development. The **core modules** of Spring are the foundational building blocks for the entire framework. Here's a breakdown of the main core modules in Spring:

---

### **1. Core Container Modules**
These modules provide the fundamental features of Spring, including dependency injection, bean configuration, and the base infrastructure.

| **Module**               | **Description**                                                                                                                                   |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Core**                 | The core module provides the fundamental features of the Spring Framework, including the **IoC (Inversion of Control)** container and **BeanFactory**. It is the foundation for the entire framework. |
| **Beans**                | This module defines the core concepts of **dependency injection (DI)** and **BeanFactory**. It manages the beans in the container and their lifecycle. |
| **Context**              | Builds on the `Beans` module to provide a more advanced configuration using **ApplicationContext**, which is the central interface for Spring-based applications. The `ApplicationContext` provides features like event propagation, declarative mechanisms, and more. |
| **Expression Language (SpEL)** | This module enables Spring’s powerful expression language, which allows querying and manipulation of object graphs at runtime. It is useful for working with beans and configuration files. |

---

### **2. AOP (Aspect-Oriented Programming) Module**
The AOP module provides support for aspect-oriented programming in Spring, which allows the separation of cross-cutting concerns (like logging, transaction management, etc.) from business logic.

| **Module**              | **Description**                                                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **AOP**                 | This module enables aspect-oriented programming (AOP) capabilities in Spring. It allows you to apply **aspects** (cross-cutting concerns) to objects, providing features like method interception, transaction management, logging, etc. |
| **Aspects**             | Part of the AOP module, this defines the application of aspects to methods within your Spring-managed beans. This module helps in creating a more modular and cleaner codebase by separating concerns like logging and security. |

---

### **3. JDBC (Java Database Connectivity) Module**
Spring provides a simplified approach to working with databases through its JDBC module, which abstracts much of the complexity in connecting to and interacting with databases.

| **Module**             | **Description**                                                                                                                        |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **JDBC**               | This module simplifies database interaction by providing a **JDBC template** for database operations, which reduces the boilerplate code of establishing connections, handling exceptions, etc. |
| **JDBC Abstraction**   | Spring provides a level of abstraction over JDBC, making database operations easier to manage and more consistent across different database types. |

---

### **4. Transaction Module**
The **transaction module** provides declarative and programmatic transaction management. It integrates with various transaction APIs, such as Java Transaction API (JTA), JDBC, and others.

| **Module**             | **Description**                                                                                                                     |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Transaction**         | This module provides a consistent abstraction for managing transactions in Spring. It supports both **declarative** and **programmatic** transaction management. It integrates with multiple transaction management strategies. |

---

### **5. Web Modules**
These modules facilitate building web applications and provide a wide range of support for HTTP, MVC, REST, and other web technologies.

| **Module**               | **Description**                                                                                                                         |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Web**                  | The **web module** provides basic web capabilities, such as multi-part file upload, simple REST capabilities, etc.                      |
| **Web MVC**              | The **Spring Web MVC** module provides a **Model-View-Controller (MVC)** architecture for developing web applications in Spring. It supports controllers, views, and other web-related features. |
| **WebSocket**            | This module allows the development of **WebSocket**-based applications using Spring. It supports full-duplex communication for web-based real-time applications. |

---

### **6. Test Module**
Spring provides a powerful **testing framework** to facilitate the testing of Spring applications. The `spring-test` module provides support for integration testing, mocking, and unit testing.

| **Module**               | **Description**                                                                                                                      |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Test**                 | This module offers support for testing Spring applications, including **JUnit** and **TestNG** integration, **mocking** dependencies, and **integration testing** of Spring beans. It provides facilities for testing the components in the application context. |

---

### **7. Messaging and Integration Modules**
These modules are used to integrate with external messaging systems, such as **JMS**, **RabbitMQ**, **Kafka**, etc.

| **Module**              | **Description**                                                                                                                         |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Messaging**           | The Spring **Messaging** module provides messaging capabilities, including integration with JMS, RabbitMQ, and other messaging systems. |
| **Integration**         | The **Spring Integration** module is used for building **enterprise integration patterns (EIP)**, providing adapters for multiple systems, and facilitating message-driven architecture. |

---

### **Summary of Core Spring Modules**

| **Module**               | **Core Purpose**                                                                                                      |
|--------------------------|------------------------------------------------------------------------------------------------------------------------|
| **Core**                 | Foundation for the framework, including IoC (Inversion of Control) and Bean management.                                |
| **Beans**                | Manages beans and dependency injection (DI) in Spring-based applications.                                             |
| **Context**              | Extends `Beans` to provide a richer application context, including support for events and application-level configuration. |
| **AOP**                  | Supports Aspect-Oriented Programming for separating cross-cutting concerns like logging and security.                |
| **JDBC**                 | Simplifies interaction with databases, reducing boilerplate code.                                                      |
| **Transaction**          | Provides transaction management (both declarative and programmatic) across various transaction systems (JTA, JDBC, etc.). |
| **Web MVC**              | Provides Model-View-Controller architecture for building web applications.                                            |
| **Test**                 | Supports testing of Spring components and applications.                                                                |

---

### **Conclusion:**
The core modules of Spring provide the essential infrastructure for building robust, scalable, and flexible applications. These modules cover everything from dependency injection to transaction management, AOP, database interaction, and web development. The modular nature of Spring allows developers to use only the modules they need, while still maintaining a consistent and unified approach to application development.

<sub>[back to top](#table-of-contents)</sub>

## **How Does the DispatcherServlet Work in Spring Boot?**

1. **Initialization:**
   - In **Spring Boot**, the **DispatcherServlet** is automatically registered and initialized by the embedded web server (Tomcat, Jetty, or Undertow). You don’t need to manually configure it.

2. **Servlet Mapping:**
   - It is mapped to handle all HTTP requests by default (e.g., `/` or `/*`), except for static resources (like images, CSS, and JS files).

3. **Request Flow:**
   - When an HTTP request is received:
     1. The **DispatcherServlet** intercepts it.
     2. It uses **HandlerMapping** to find the appropriate controller.
     3. The controller method is invoked.
     4. A **ModelAndView** (model and view name) is returned from the controller.
     5. A **ViewResolver** resolves the view and renders the response.

---

In summary, **DispatcherServlet** acts as the central controller in Spring Boot, routing requests to the correct controllers and rendering views based on the return values from the controller methods.

<sub>[back to top](#table-of-contents)</sub>


## What is Spring Boot Actuator?
Spring Boot Actuator is a set of tools to help monitor and manage Spring Boot applications in production. It provides various endpoints for health checks, metrics, and environment details.

<sub>[back to top](#table-of-contents)</sub>

## What are some commonly used endpoints in Spring Boot Actuator?
Some common endpoints include:
/actuator/health: Displays health status of the application.
/actuator/metrics: Exposes application performance metrics.
/actuator/env: Shows environment properties.
/actuator/info: Provides application metadata like version and build information.

<sub>[back to top](#table-of-contents)</sub>

## Changing Property at Runtime
In Spring, to change properties at runtime, you can use:

1. **Environment Interface**: Access properties at runtime using `Environment`, but it doesn't support direct updates.
2. **`@ConfigurationProperties`**: Bind properties to beans and reload them from external sources like a database.
3. **Spring Cloud Config**: Use for centralized configuration management with dynamic updates via `/actuator/refresh`.
4. **`@RefreshScope`**: Automatically refresh beans with new properties when the configuration is updated (works with Spring Cloud).

For dynamic changes, **Spring Cloud Config** is the most common solution.

<sub>[back to top](#table-of-contents)</sub>

## Aspect Oriented Programming (AOP)
**Aspect-Oriented Programming (AOP)** in Spring is a programming paradigm that allows separating cross-cutting concerns (e.g., logging, security, transactions) from the core business logic. AOP helps in modularizing the code by applying behaviors like logging, transaction management, and security across multiple methods without modifying the actual code of those methods.

### Key Concepts:
1. **Aspect**: A module that contains cross-cutting concerns (e.g., logging, caching).
2. **Join Point**: A point in the program execution where an aspect can be applied (e.g., method execution).
3. **Advice**: The code that is executed at a join point. Types of advice:
   - **Before**: Runs before a method execution.
   - **After**: Runs after a method execution (regardless of success/failure).
   - **After Returning**: Runs after a successful method execution.
   - **After Throwing**: Runs if the method throws an exception.
   - **Around**: Wraps method execution, allowing you to modify input/output or control the flow.

4. **Pointcut**: A predicate that matches join points, helping to define where advice should be applied.
5. **Weaving**: The process of applying aspects to target objects. This happens at runtime, compile-time, or load-time.

### Example of AOP in Spring:

1. **Define an Aspect:**
   ```java
   @Aspect
   @Component
   public class LoggingAspect {
       @Before("execution(* com.example.service.*.*(..))")
       public void logBefore(JoinPoint joinPoint) {
           System.out.println("Before method: " + joinPoint.getSignature().getName());
       }
   }
   ```

2. **Enable AOP in Spring Configuration:**
   ```java
   @Configuration
   @EnableAspectJAutoProxy
   public class AppConfig {
   }
   ```

### Use Cases:
- **Logging**: Automatically log method entry and exit.
- **Security**: Implement authentication and authorization across various methods.
- **Transactions**: Manage transactions declaratively across methods.
  
AOP in Spring improves modularity, promotes cleaner code, and enhances maintainability by separating concerns that are not part of the business logic.

<sub>[back to top](#table-of-contents)</sub>

## @ControllerAdvice
The @ControllerAdvice annotation in Spring is used to define a global exception handler for all controllers in a Spring application.

<sub>[back to top](#table-of-contents)</sub>

## Stream Vs for Loop

| **Feature**              | **Stream**                                      | **for loop**                                 |
|--------------------------|-------------------------------------------------|---------------------------------------------|
| **Programming Style**     | Declarative (focuses on what to do)             | Imperative (focuses on how to do it)        |
| **Parallelism**           | Can be easily parallelized (`parallelStream()`) | Manual handling of parallelism required     |
| **Iteration**             | Internal iteration (handled by Stream API)      | External iteration (explicit loop control)  |
| **Evaluation**            | Lazy evaluation (operations executed when terminal operation is invoked) | Immediate execution of loop logic          |
| **Readability**           | More concise, especially for complex transformations | More verbose, especially for complex logic |
| **Side Effects**          | Should avoid side effects (pure functional style) | Can have side effects (modifying external states) |
| **Performance**           | May be optimized (parallelism and optimizations by Stream API) | Typically faster for simple tasks         |
| **Example**               | `numbers.stream().filter(x -> x % 2 == 0).forEach(System.out::println)` | `for (int num : numbers) { if (num % 2 == 0) { System.out.println(num); } }` |

### Conclusion:
- **Streams** are ideal for functional-style, concise, and chainable operations with the advantage of parallelism and lazy evaluation.
- **for loops** are more straightforward and offer fine control over iteration, especially for simpler tasks.

<sub>[back to top](#table-of-contents)</sub>
