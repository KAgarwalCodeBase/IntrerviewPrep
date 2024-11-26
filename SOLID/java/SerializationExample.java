import java.io.*;

class Address implements Serializable {
    String city;

    Address(String city) {
        this.city = city;
    }
}

class Person implements Serializable {
    String name;
    Address address;

    Person(String name, Address address) {
        this.name = name;
        this.address = address;
    }

    // Deep copy using serialization
    public Person deepCopy() throws IOException, ClassNotFoundException {
        // Serialize the object
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(bos);
        oos.writeObject(this);

        // Deserialize the object
        ByteArrayInputStream bis = new ByteArrayInputStream(bos.toByteArray());
        ObjectInputStream ois = new ObjectInputStream(bis);
        return (Person) ois.readObject();
    }
}

public class SerializationExample {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        Address address = new Address("New York");
        Person p1 = new Person("John", address);

        // Create a deep copy
        Person p2 = p1.deepCopy();

        System.out.println(p1.address.city); // Output: New York
        p2.address.city = "Los Angeles"; // Modify the copied object
        System.out.println(p1.address.city); // Output: New York (not affected)
        System.out.println(p2.address.city);
    }
}
