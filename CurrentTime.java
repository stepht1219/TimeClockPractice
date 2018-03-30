//Stephanie Tattrie
//CurrentTime.java
//here we go againnnnn

import java.text.SimpleDateFormat;
import java.util.Calendar;


public class CurrentTime{

	public static void main(String[] args){
		Calendar cal = Calendar.getInstance();
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-mm-dd hh:mm");
		System.out.println(sdf.format(cal.getTime()));
	}
}