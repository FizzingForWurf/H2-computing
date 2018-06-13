import java.net.URL;
import java.io.*;
import java.util.Scanner;

public class OpenFile {
    
    public static void main(String[] args) {
        File file = new File("src\\java_testing.txt");
        
        try {
            Scanner sc = new Scanner(file);

            while (sc.hasNextLine()){
                String line = sc.nextLine();
                System.out.println(line);
            }

            sc.close();
            System.out.println("DONE!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
