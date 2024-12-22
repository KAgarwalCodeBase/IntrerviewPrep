public class CloneFactory {
    public Animal getClone(Animal obj){
        try {
            return obj.makeCopy();
        } catch (CloneNotSupportedException e) {
            throw new RuntimeException(e);
        }
    }
}
