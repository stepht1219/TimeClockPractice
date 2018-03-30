//Stephanie Tattrie
//Date.java
//Hopefully I can figure out how to access the date and make it readable.

import java.sql.Date.*;

public class Date{

	public static void main(String[] args){
		Date rightNow = new Date();
		String dateNow = rightNow.toString();
		//String dateNow = rightNow.toLocalDate();
		System.out.println(dateNow);
	}
}