package lab1;

import java.util.Scanner;

public class task3 {
	public static int computeScore(String word) {
		int score =0;
		for(int i=0; i<word.length();i++) {
			
			char c= word.charAt(i);
			switch(c) {
				case 'a':
					score+=1;
					break;
				case 'b':
					score+=3;
					break;
				case 'c':
					score+=3;
					break;
				case 'd':
					score+=2;
					break;
				case 'e':
					score+=1;
					break;
				case 'f':
					score+=4;
					break;
				case 'g':
					score+=2;
					break;
				case 'h':
					score+=4;
					break;
				case 'i':
					score+=1;
					break;
				case 'j':
					score+=8;
					break;
				case 'k':
					score+=5;
					break;
				case 'l':
					score+=1;
					break;
				case 'm':
					score+=3;
					break;
				case 'n':
					score+=1;
					break;
				case 'o':
					score+=1;
					break;
				case 'p':
					score+=3;
					break;
				case 'q':
					score+=10;
					break;
				case 'r':
					score+=1;
					break;
				case 's':
					score+=1;
					break;
				case 't':
					score+=1;
					break;
				case 'u':
					score+=1;
					break;
				case 'v':
					score+=4;
					break;
				case 'w':
					score+=4;
					break;
				case 'x':
					score+=8;
					break;
				case 'y':
					score+=4;
					break;
				case 'z':
					score+=10;
					break;
				default:
					score+=0;
					break;
			}
		}
		return score;
	}
	public static void main(String[] args) {
		Scanner input= new Scanner(System.in);
		System.out.println("Please enter the string");
		String word=input.next();
		word= word.toLowerCase();
		
		int score=computeScore(word);
		System.out.println(score);

	}
}
