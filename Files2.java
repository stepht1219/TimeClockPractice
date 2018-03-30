//Stephanie Tattrie
//Files2.java
//7/3/17
//Program to make and move files from one directory to another

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

public class Files2{

        public static void main(String[] args){
                Path moveFrom = FileSytems.getDefault().getPath("/Users/stephanietattrie/Documents/Practice.txt"); //This is the original path
                Path dest = FileSystems.getDefault().getPath("/Users/stephanietattrie/Desktop"); //This is the destination path
                Path destDir = FileSystems.getDefault().getPath("/Users/stephanietattrie/Desktop");
        try{
                Files.move(moveFrom, dest, StandardCopyOption.REPLACE_EXISTING);
        }
        catch(IOException e){
                System.err.println(e);
        }

        }
}
