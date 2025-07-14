import java.util.Scanner;

public class BarChartPrinting {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        for(int num = 1; num <= 5; num++){
            System.out.print("Please enter a number between 1 and 30: ");
            int number = input.nextInt();

            while(number < 1 || number > 30){
                System.out.print("Please enter a number between 1 and 30: ");
                number = input.nextInt();
            }
            for(int asterick = 1; asterick <= number; asterick++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
