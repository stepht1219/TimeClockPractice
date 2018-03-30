// Java program to illustrate renaming and
// moving a file permanently to a new loaction
import java.io.*;
import java.nio.file.Files;
import java.nio.file.*;
 
public class TestMoveFile
{
    public static void main(String[] args) throws IOException
    {
        Path temp = Files.move
        (Paths.get("/Users/stephanietattrie/Documentsq/Test.txt"), 
        Paths.get("/Users/stephanietattrie/Documents/2017/Text.txt"));
 
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