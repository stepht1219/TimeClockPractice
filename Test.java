import java.io.*;
import java.nio.file.Files.*;
import java.nio.file.*;
 
public class Test
{
    public static void main(String[] args) throws IOException 
    {
        Path temp = Files.move
        (Paths.get("C://Users/stephanietattrie/Documents/Practice.txt"), 
        Paths.get("C://Users/stephanietattrie/Desktop"));
 
        if(temp != null)
        {
            System.out.println("File renamed and moved successfully");
        }
        else
        {
            System.out.println("Failed to move the file");
        }
    }
}