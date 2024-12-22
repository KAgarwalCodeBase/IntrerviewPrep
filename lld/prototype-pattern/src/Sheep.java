public class Sheep implements Animal{
    public Sheep(){
        System.out.println("Sheep is being made.");
    }
    @Override
    public Animal makeCopy() {
        System.out.println("Sheep is Being Made");

        Animal obj = null;
        try {
            obj = (Animal)super.clone();
        } catch (CloneNotSupportedException e) {
            System.out.println("The Sheep was Turned to Mush");

            throw new RuntimeException(e);
        }
        return obj;
    }

    public String toString(){
        return "Dolly is my hero! Baaa!";
    }
}
