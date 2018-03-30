//this is another test to see how to properly implement date formatter and calendar classes

import java.text.SimpleDateFormat;
import java.util.Calendar;

public class TimeTest{
	public static void main(String[]args){
		Calendar cal = Calendar.getInstance();
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd hh:mm");
		String currentDate = sdf.format(cal.getTime()); 
		System.out.println(currentDate);
	}
}