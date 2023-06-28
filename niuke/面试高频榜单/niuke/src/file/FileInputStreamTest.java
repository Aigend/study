package file;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

class FileInputStreamTest {
    public static void main(String[] args) throws IOException {

        FileInputStream fileInputStream = new FileInputStream("D:\\wenlong\\github\\study\\niuke\\面试高频榜单\\niuke\\src\\file\\read.txt");
        byte[] buf = new byte[1024];
        int hasRead = 0;
        while ((hasRead=fileInputStream.read(buf)) > 0){
            System.out.println(new String(buf, 0 , hasRead));
        }

    }
}
