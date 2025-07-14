import java.util.Scanner;
public class SalesCommissionCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double wages = 200.0;
        double commissionRate = 0.09;
        double totalSales = 0.0;

        System.out.println("Enter the price of each item sold: ");
        System.out.print("Enter -1 when you're done: ");

        while(true) {
            System.out.print("Item price: $");
            double itemPrice = input.nextDouble();
            if (itemPrice == -1)  break;
            if (itemPrice <= 0) {
                System.out.println("Invalid price entered. Please try again.");
                continue;
            }
            totalSales += itemPrice;
        }
        double commission = totalSales * commissionRate;
        double totalEarnings = commission + wages;
System.out.printf("Total sales of: $%.2f%n", totalSales);
System.out.printf("commission of 9%: $%.2f%n" + commission);
System.out.printf("Total earnings: $%.2f" + totalEarnings);




    }
}
