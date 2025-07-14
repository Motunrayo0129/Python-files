import java.util.Scanner;

public class Comparator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

            System.out.print("Enter a number: ");
            int number1 = input.nextInt();

            System.out.print("Enter a number: ");
            int number2 = input.nextInt();

            if (number1 == number2) {
                System.out.println("0");
            }
            else if(number1 > number2){
                System.out.println("1");
            }
            else if(number1 < number2){
                System.out.println("-1");
            }

    }
}
