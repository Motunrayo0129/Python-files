import java.util.Scanner;

public class ModifiedDiamondPrinting {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n;
        do {
            System.out.print("Enter an odd number between 1 and 19: ");
            n = input.nextInt();
        } while (n < 1 || n > 19 || n % 2 == 0);

        int mid = (n + 1) / 2;

        for (int row = 1; row <= mid; row++) {
            for (int space = 1; space <= mid - row; space++) {
                System.out.print("  ");
            }
            for (int star = 1; star <= 2 * row - 1; star++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        for (int row = mid - 1; row >= 1; row--) {
            for (int space = 1; space <= mid - row; space++) {
                System.out.print("  ");
            }
            for (int star = 1; star <= 2 * row - 1; star++) {
                System.out.print("* ");
            }
            System.out.println();
        }


    }
}
