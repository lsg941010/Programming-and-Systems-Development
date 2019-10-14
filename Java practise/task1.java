
package lab1;
import java.util.*;
public class task1 {

	public static void printPrimes(int max) {
		
		int[] primenumber= new int[max];
		int count=0;
		for (int i=1;i<=max;i++) {
			
			
			boolean prime=true;
			for(int j=2; j<i;j++) {
				if(i%j==0) {
					prime=false;
					break;
				}
			}
			if (prime==true) {
				primenumber[count]=i;
				
				count= count+1;
				
			}
		}
		int[] thefinal=new int[count];
		for(int k=0;k<count;k++) {
			thefinal[k]=primenumber[k];
		}
		System.out.println(Arrays.toString(thefinal));
	}

	public static void main(String[] args) {
		Scanner input= new Scanner(System.in);
		System.out.println("Please enter an integer");
		int number=input.nextInt();
		System.out.println("Calculating the prime numbers");
		printPrimes(number);

	}

}
