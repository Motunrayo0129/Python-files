import java.util.Scanner;

public class GasMileage {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double totalGallons = 0;
        double totalMiles = 0;

        while (true) {
            System.out.print("Enter miles cover or(-1 to exit): ");
            double miles = input.nextInt();
            totalMiles += miles;
            if (miles == -1) {
                break;
            }

            System.out.print("Enter gallons cover: ");
            double gallons = input.nextInt();
            totalGallons += gallons;

            double mpGallons = miles / gallons;
            System.out.printf("The miles per gallon is $%.2f: ", mpGallons);
        }
            if (totalGallons > 0) {
               double overAllMpGallons = totalMiles / totalGallons;
               System.out.printf("The overall average mile/gallons was %.2f%n", overAllMpGallons);

            }
            else{
                System.out.println("Please enter a positive integer");
            }

    }
}
