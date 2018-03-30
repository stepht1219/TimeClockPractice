package test;

import java.io.File;
import java.io.IOException;

import org.apache.commons.io.FileUtils;

public class MoveFileToDirectoryTest {

	public static void main(String[] args) throws IOException {

		File sourceFile = new File("/Users/stephanietattrie/Documents/Hydrogen Spectrum.docx");
		File destinationDir = new File("/Users/stephanietattrie/Movies");

		FileUtils.moveFileToDirectory(sourceFile, destinationDir, true);

	}

}