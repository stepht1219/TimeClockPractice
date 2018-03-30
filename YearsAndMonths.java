//This is to try and use the years and months in a loop

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.*;
import java.io.File.*;
import java.io.*;
import javax.swing.JFrame;



public class YearsAndMonths{
	public static void main(String[] args){}

     
    
		Calendar cal = Calendar.getInstance();
		int minutes = Calendar.getInstance().get(Calendar.MINUTE);
		/*SimpleDateFormat minutes = new SimpleDateFormat("mm");
		try{
			int newmin = Integer.parseInt(minutes);
		}
		catch(NumberFormatException ex){

		}
		int newmin = Integer.parseInt(minutes);*/

		if (minutes == minutes + 1){
			File file = new File("Something");
       	    if (!file.exists()) {
               if (file.mkdir()) {
                   System.out.println("Directory is created!");
               } else {
                   System.out.println("Failed to create directory!");
            }
        }
		}


		
    }
		
	}
