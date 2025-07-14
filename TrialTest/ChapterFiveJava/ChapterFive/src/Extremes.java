import java.util.Scanner;

public class Extremes {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("How many numbers would you like to enter? : ");
        int num = input.nextInt();
        int max = - 1000000000;
        int min = 1000000000;
        int sum = 0;
        for(int numbers = 1; numbers <= num; numbers++) {
            System.out.print("Enter number " + numbers + ": ");
            int number = input.nextInt();

            if(number < min) {
                min = number;
            }
            if(number > max) {
                max = number;
            }
            sum = max + min;
        }
        System.out.println("The maximum number is " + max);
        System.out.println("The minimum number is " + min);
        System.out.println("\n The sum is " + sum);




    }
}
