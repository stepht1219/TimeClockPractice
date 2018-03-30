//Stephanie Tattrie
//I'm still trying to move one file to another location
//7/5/17

import java.io.*;
import java.nio.file.Files.*;
import java.nio.file.*;

public class Test2{

	public static void main(String[] args){
		try{
			File myFile = new File("//Users/stephanietattrie/Documents/Practice.txt");

			if(myFile.renameTo(new File("//Users/stephanietattrie/Desktop" + myFile.getName()))){
				System.out.println("File was moved successfully :)");
			}

			else{
				System.out.println("File failed to move :(");
			}
		}
		catch(Exception e){
			e.printStackTrace();
		}


	}


}//renameTo doesnt move it, it literally just adds the name to the end???

//i'm not sure how any of this works omg someone please help me


