//Stephanie Tattrie
//MkDir.java

//This program is to make a new directory/folder.
import java.util.*;
import java.io.File.*;
import java.io.*;

public class MkDir{

	public static void main(String[] args){
		//System.out.println("What would you like to call the new folder?");
		//Scanner stdin = new Scanner(System.in);
		File file = new File("2017");
        if (!file.exists()) {
            if (file.mkdir()) {
                System.out.println("Directory is created!");
            } else {
                System.out.println("Failed to create directory!");
            }
        }



	}



}