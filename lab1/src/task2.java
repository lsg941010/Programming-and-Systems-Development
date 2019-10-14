package lab1;
import java.util.*;
public class task2 {
	public static int computeFibonacci (int n) {
		if(n<=1) {
			return n;
		}
		return computeFibonacci(n-1)+computeFibonacci(n-2);
	}
	public static void main(String[] args) {
		Scanner input= new Scanner(System.in);
		System.out.println("Please enter the Nth Fibonacci number");
		int number=input.nextInt();
		int result=computeFibonacci(number);
		System.out.println(result);
//ArrayList could be another way of doing this
	}

}
