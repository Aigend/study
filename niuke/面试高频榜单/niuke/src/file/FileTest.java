package file;

import java.io.File;

class FileTest {
    public static void main(String[] args) {
        File file = new File(".");
        System.out.println(file.getName());
        System.out.println(file.getPath());
        System.out.println(file.getAbsolutePath());
        System.out.println(file.getParent());

    }
}
