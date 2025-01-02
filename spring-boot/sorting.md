```java
Collections.sort(studentList, new Comparator<Student>() {
    @Override
    public int compare(Student s1, Student s2) {
        // Compare by CGPA (descending order)
        if (Double.compare(s2.getCgpa(), s1.getCgpa()) != 0) {
            return Double.compare(s2.getCgpa(), s1.getCgpa());
        }
        // Compare by first name (alphabetical order)
        if (!s1.getFname().equals(s2.getFname())) {
            return s1.getFname().compareTo(s2.getFname());
        }
        // Compare by ID (ascending order)
        return Integer.compare(s1.getId(), s2.getId());
    }
});
        
```