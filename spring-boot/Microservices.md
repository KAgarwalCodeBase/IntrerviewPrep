## Table of Contents

-   [FeignClient: For Make HTTP calss to extral API's.](#feignclient-for-make-http-calss-to-extral-apis)
-   [Service Registry](#what-is-a-service-registry)
- [API Gateway](#api-gateway)
For API Gateway 
spring-cloud-starter-gateway


### FeignClient: For Make HTTP calss to extral API's.

`FeignClient` is a declarative REST client in Spring Boot, used for making HTTP calls to external APIs in a more concise and readable way. It eliminates boilerplate code for creating REST clients by using annotations.

### Key Features of `FeignClient`:
1. **Declarative Approach**: Write interfaces annotated with `@FeignClient`, and Feign handles the REST client logic.
2. **Integration with Ribbon/Eureka**: Supports load balancing and service discovery when integrated with Netflix Ribbon or Spring Cloud Netflix Eureka.
3. **Customizable**: Allows customization of request interceptors, error handling, and logging.

### Adding Feign to Your Project
To use `FeignClient` in a Spring Boot project:
1. Add the required dependency in your `pom.xml` (for Maven):
   ```xml
   <dependency>
       <groupId>org.springframework.cloud</groupId>
       <artifactId>spring-cloud-starter-openfeign</artifactId>
   </dependency>
   ```
   Or in `build.gradle` (for Gradle):
   ```gradle
   implementation 'org.springframework.cloud:spring-cloud-starter-openfeign'
   ```
   Ensure you have the correct version compatible with your Spring Boot version.

2. Enable Feign support by adding `@EnableFeignClients` in a configuration class or the main application class:
   ```java
   @SpringBootApplication
   @EnableFeignClients
   public class FeignExampleApplication {
       public static void main(String[] args) {
           SpringApplication.run(FeignExampleApplication.class, args);
       }
   }
   ```

### Creating a Feign Client
Create an interface annotated with `@FeignClient` to define the remote service:
```java
@FeignClient(name = "example-service", url = "https://api.example.com")
public interface ExampleClient {

    @GetMapping("/endpoint")
    ResponseEntity<String> getExampleData();

    @PostMapping("/endpoint")
    ResponseEntity<String> createExampleData(@RequestBody ExampleRequest request);
}
```

### Making a Call
Use the Feign client by injecting it into your Spring-managed components:
```java
@Service
public class ExampleService {
    private final ExampleClient exampleClient;

    public ExampleService(ExampleClient exampleClient) {
        this.exampleClient = exampleClient;
    }

    public String getData() {
        return exampleClient.getExampleData().getBody();
    }
}
```

### Advanced Features
1. **Path Variables and Query Parameters**:
   ```java
   @GetMapping("/endpoint/{id}")
   ResponseEntity<String> getExampleDataById(@PathVariable("id") String id);

   @GetMapping("/endpoint")
   ResponseEntity<String> getExampleDataByQuery(@RequestParam("param") String param);
   ```

2. **Custom Configurations**:
   You can define specific configurations for a Feign client:
   ```java
   @FeignClient(name = "example-service", configuration = CustomFeignConfig.class)
   public interface ExampleClient { ... }
   ```

   Example `CustomFeignConfig`:
   ```java
   @Configuration
   public class CustomFeignConfig {
       @Bean
       public RequestInterceptor requestInterceptor() {
           return requestTemplate -> requestTemplate.header("Authorization", "Bearer token");
       }
   }
   ```

3. **Error Handling**:
   Use `@ControllerAdvice` or Feign's error decoder:
   ```java
   @Component
   public class CustomErrorDecoder implements ErrorDecoder {
       @Override
       public Exception decode(String methodKey, Response response) {
           return new RuntimeException("Custom error message");
       }
   }
   ```

4. **Feign Logging**:
   Enable logging by adding the following to `application.properties` or `application.yml`:
   ```properties
   logging.level.feign=DEBUG
   logging.level.<your.package.name>.ExampleClient=DEBUG
   ```

With Feign, you can reduce boilerplate code, making your codebase cleaner and easier to maintain.

<sub>[back to top](#table-of-contents)</sub>

### **What is a Service Registry?**

A **Service Registry** is a critical component in a microservices architecture. It acts as a centralized directory that dynamically keeps track of all the services, their instances, and their locations (e.g., IP addresses, ports). In essence, it enables **service discovery**, allowing microservices to find and communicate with each other without hardcoding the endpoints.

### **Example with Netflix Eureka**

Using **Netflix Eureka**, let's illustrate how a service registry works with the setup we just configured.

---

### **1. Service Registry (Eureka Server)**

The **Eureka Server** acts as the service registry. It maintains a list of services registered with it, along with their metadata (IP, port, health status, etc.). Services register themselves with the server upon startup and deregister when they shut down.

#### Code Example for Eureka Server:
```java
@SpringBootApplication
@EnableEurekaServer
public class EurekaServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(EurekaServerApplication.class, args);
    }
}
```

#### Configuration in `application.properties`:
```properties
spring.application.name=eureka-server
server.port=8761

eureka.client.register-with-eureka=false
eureka.client.fetch-registry=false
```

- **Purpose**: Hosts the registry at `http://localhost:8761`.

When you start the Eureka server, you can view the registry dashboard at `http://localhost:8761`. At first, it will show an empty list of registered services.

---

### **2. Service Registration (Eureka Client)**

When a service (e.g., `eureka-client`) starts, it automatically registers itself with the Eureka server. The server keeps track of its name, IP address, port, and health status.

#### Code Example for a Eureka Client:
```java
@SpringBootApplication
@EnableEurekaClient
public class EurekaClientApplication {
    public static void main(String[] args) {
        SpringApplication.run(EurekaClientApplication.class, args);
    }
}
```

#### Configuration in `application.properties`:
```properties
spring.application.name=eureka-client
server.port=8080

eureka.client.service-url.defaultZone=http://localhost:8761/eureka/
eureka.instance.prefer-ip-address=true
```

- **Purpose**: Registers itself with the Eureka server (`defaultZone`) and uses its IP address (`prefer-ip-address`).

When this service starts, it sends a registration request to the Eureka server. The server now shows `eureka-client` in the dashboard, along with its details.

---

### **3. Service Discovery**

When another service (e.g., `another-client`) needs to communicate with `eureka-client`, it doesn't need to know the exact location (IP/port). Instead, it queries the **Eureka server** to discover the current instance of `eureka-client`.

#### Example of Service Discovery with `RestTemplate`:
```java
@Service
public class GreetingService {
    private final RestTemplate restTemplate;

    public GreetingService(RestTemplateBuilder restTemplateBuilder) {
        this.restTemplate = restTemplateBuilder.build();
    }

    public String getGreeting() {
        String url = "http://eureka-client/greeting"; // Service name
        return restTemplate.getForObject(url, String.class);
    }
}
```

#### Configuration for Load Balancing in `application.properties`:
```properties
spring.application.name=another-client
server.port=8081

eureka.client.service-url.defaultZone=http://localhost:8761/eureka/
eureka.instance.prefer-ip-address=true
```

- **Service Call**: When `another-client` calls `http://eureka-client/greeting`, Eureka resolves `eureka-client` to its actual location (e.g., `http://localhost:8080`).

---

### **How the Service Registry Works in This Example**

1. **Eureka Server (Service Registry)**:
   - Hosts the registry and dynamically tracks all registered services.

2. **Eureka Clients (Services)**:
   - `eureka-client` and `another-client` register themselves with the Eureka server.
   - Registration includes metadata such as the service name, IP address, port, and health status.

3. **Service Discovery**:
   - `another-client` doesn't need the exact IP/port of `eureka-client`.
   - It queries the Eureka server, which provides the active instance of `eureka-client`.

4. **Dynamic Scaling**:
   - If more instances of `eureka-client` are started, they are also registered with Eureka.
   - The registry dynamically updates, and `another-client` can load balance requests across all instances.

---

### **Benefits of Using a Service Registry**
1. **Dynamic Service Discovery**:
   - No hardcoding of service locations. Services query the registry to get the latest location.

2. **Fault Tolerance**:
   - If a service goes down, it is deregistered, preventing requests to unreachable services.

3. **Scalability**:
   - Handles dynamic scaling of services. New instances are automatically registered and discoverable.

4. **Centralized Management**:
   - All service information is maintained in one place, simplifying management.

5. **Load Balancing**:
   - Clients can use the registry to load balance requests across multiple instances of a service.

---

### **Conclusion**

In this example, the **Netflix Eureka Server** is the **Service Registry**. It acts as the backbone of service discovery, enabling `eureka-client` and `another-client` to interact dynamically without hardcoded endpoints. This setup provides a scalable and fault-tolerant architecture for microservices.

<sub>[back to top](#table-of-contents)</sub>



### **API Gateway**

An **API Gateway** is a server that acts as an entry point for all client requests to backend services, handling tasks such as routing, security, monitoring, and traffic management.

---

### **Core Functions**:
1. **Request Routing**: Directs requests to the appropriate backend service.
2. **Security**: Handles authentication, authorization, and threat protection.
3. **Traffic Management**: Manages rate limiting, throttling, and caching.
4. **Monitoring**: Provides logging and performance metrics.
5. **Data Transformation**: Modifies request/response formats when necessary.

---

### **Popular API Gateway Tools**:
- **Spring Cloud Gateway**: Lightweight, flexible, and built on Spring. Integrates well with Spring applications.
- **Kong**: Scalable and open-source, built on NGINX.
- **AWS API Gateway**: Managed service by AWS, supports REST, HTTP, and WebSocket APIs.
- **Apigee**: Enterprise-grade API management.

---

### **Spring Cloud Gateway** Configuration Example:
1. **Add Dependency**:
   ```xml
   <dependency>
       <groupId>org.springframework.cloud</groupId>
       <artifactId>spring-cloud-starter-gateway</artifactId>
   </dependency>
   ```

2. **Configure Routes** in `application.properties`:
```properties
server.port=8083
spring.application.name=API-GATEWAY

#routes  configuration

spring.cloud.gateway.routes[0].id=QUIZ-SERVICE
spring.cloud.gateway.routes[0].uri=lb://QUIZ-SERVICE
spring.cloud.gateway.routes[0].predicates[0]=Path= /quiz/**, /quiz-test/**


spring.cloud.gateway.routes[1].id=QUESTION-SERVICE
spring.cloud.gateway.routes[1].uri=lb://QUESTION-SERVICE
spring.cloud.gateway.routes[1].predicates[0]=Path= /question/**
```
3. **Enable Feign Client or Custom Filters** for enhanced control, security, and logging.

---

### **Benefits**:
- **Centralized Management**: Simplifies security, routing, and monitoring.
- **Improved Performance**: Caching, load balancing, and rate limiting.
- **Scalable and Flexible**: Easy to scale and modify routing logic.

---

API Gateways help manage microservice communication, ensuring efficient and secure interaction between clients and backend services.


<sub>[back to top](#table-of-contents)</sub>

