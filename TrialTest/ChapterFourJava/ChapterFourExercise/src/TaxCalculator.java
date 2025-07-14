import java.util.Scanner;
public class TaxCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double lowerRate = 0.15;
        double upperRate = 0.20;

        for (int num = 1; num <= 3; num++) {
            System.out.printf("\nCitizen", + num);

            System.out.print("Enter name: ");
            String name = input.nextLine();

            System.out.print("Enter annual earning in USSD: ");
            double annualEarning = input.nextDouble();
            input.nextLine();

            double tax;
            if (annualEarning <= 30_000) {
               tax = annualEarning * lowerRate;
            }
            else {
                tax = annualEarning * upperRate;
            }
            System.out.printf("%s will pay a total tax of $%.2f%n", name, tax);



        }


    }

}
