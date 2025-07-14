import java.util.Scanner;

public class RightAngledTriangle {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the base of the triangle (1–10): ");
        int base = input.nextInt();

        if (base >= 1 && base <= 10) {
            for (int row = 1; row <= base; row++) {
                for (int col = 1; col <= row; col++) {
                    System.out.print("*");
                }
                System.out.println();
            }
        } else {
            System.out.println("Please enter a number between 1 and 10.");
        }
    }
}