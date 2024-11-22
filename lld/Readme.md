### Encapsulation: It's protect our data.

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

## Inheritance
![Inheritance1](./assets/inheritance1.png)
![Inheritance1](./assets/inheritance2.png)
![Inheritance1](./assets/inheritance3.png)


### We cann't use non-static variable and methods inside static method.
