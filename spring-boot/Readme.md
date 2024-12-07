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


