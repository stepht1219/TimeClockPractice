//Stephanie Tattrie
//ClockTest2.java
//instead of using the Calendar class I'm going to try using the Clock class and make sure it's accurate.

import java.lang.System.*;
import java.util.Date.*;
import java.sql.Date.*;
import java.util.*;
import java.text.DateFormat.*;

public class ClockTest2{

	public static void main(String[] args){
		Date date = new Date(logEvent.timeStamp);
		DateFormat formatter = new SimpleDateFormat("HH:mm:ss:SSS");
		String dateFormatted = formatter.format(date);
		System.out.println(dateFormatted);
	}
}