import java.util.Scanner;

public class CreditLimitCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of customers: ");
        int customerCount = input.nextInt();

        for (int num = 1; num <= customerCount; num++) {

            System.out.println("Customer #" + num + ":. Enter" );
            System.out.print("Account Number: ");
            int accountNumber = input.nextInt();

            System.out.print("Starting balance: ");
            double startingBalance = input.nextDouble();

            System.out.print("Enter credit applied this month: ");
            double creditApplied = input.nextDouble();

            System.out.print("Credit limit: ");
            double creditLimit = input.nextInt();

            System.out.print("Total charges applied this month: ");
            double chargesApplied = input.nextDouble();

            double newBalance = startingBalance + chargesApplied - creditApplied;
            System.out.println("New balance for account " + accountNumber + " is $" + newBalance);
            if(newBalance > creditLimit) {
                System.out.println("Credit limit is exceeded");

            } else {
                System.out.println("Within credit limit");
            }


        }
    }
}
