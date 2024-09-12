import java.io.*;
import java.util.*;

class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
        int num = Integer.parseInt(br.readLine());
		
		int[] array = new int[11];
		
		array[0] = 0;
		array[1] = 1;
		array[2] = 2;
		array[3] = 4;
		

		int a = 0;
		for(int i = 0; i < num; i++) {
			a = Integer.parseInt(br.readLine());
			for(int j = 4; j <= a; j++) {
				array[j] = array[j - 1] + array[j - 2] + array[j - 3];
			}
			System.out.println(array[a]);
		}
	}

}
