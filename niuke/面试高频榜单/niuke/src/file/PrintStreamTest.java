package file;

import java.io.*;

class PrintStreamTest {
    public static void main(String[] args) {
//        try (FileOutputStream fileOutputStream = new FileOutputStream("readme.txt");
//             PrintStream printStream = new PrintStream(fileOutputStream))
//        {
//            printStream.println("readme aaaa.txt");
//        } catch (IOException ioe){
//            ioe.printStackTrace();
//        }

        try (FileInputStream fileInputStream = new FileInputStream("readme.txt");
             PrintWriter printWriter = new PrintWriter(fileInputStream.toString());)
        {
            printWriter.println("打印成功");
        } catch (IOException ioe){
            ioe.printStackTrace();
        }

    }
}
