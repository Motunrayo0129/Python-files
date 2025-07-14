import java.util.Scanner;
public class LargestUnitSold {
public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    int largestUnitSold = 0;
    for (int n = 1; n <= 10; n++) {
        System.out.print("Enter number of units sold: ");
        int sold = input.nextInt();

        if (sold > largestUnitSold) {
            largestUnitSold = sold;
        }
    }
        System.out.println("Largest Unit Sold: " + largestUnitSold);

}
}