import java.util.Scanner;
public class Palindrome {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a five digit number: ");
        int number = input.nextInt();

        if (number >= 10000 ||  number <= 99999) {
            int firstDigit = number / 10000;
            int secondDigit = (number / 1000) % 10;
            int thirdDigit = (number / 100) % 10;
            int fourthDigit = (number / 10) % 10;
            int fifthDigit = number % 10;

            if (firstDigit == fifthDigit && secondDigit == fourthDigit) {
                System.out.println("The number is a palindrome");
            }
            else {
                System.out.println("The number is not a palindrome");
            }
        }
        else{
            System.out.println("Please enter a five digit number: ");
        }
    }
}
