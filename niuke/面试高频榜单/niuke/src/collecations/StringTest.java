package collecations;

public class StringTest {
    public static void main(String[] args) {
        String s = "ABC";
        String t = "abc";

        System.out.println(s.charAt(0));

        System.out.println(s.concat("##"));

        System.out.println(s);

        System.out.println(s.compareTo(t));

        System.out.println(s.compareToIgnoreCase(t));

        System.out.println();
    }
}
