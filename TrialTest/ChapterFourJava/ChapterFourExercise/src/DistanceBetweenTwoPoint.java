import java.util.Scanner;

public class DistanceBetweenTwoPoint {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter x1: ");
        int x1 = input.nextInt();
        System.out.print("Enter y1: ");
        int y1 = input.nextInt();

        System.out.print("Enter x1: ");
        int x2 = input.nextInt();
        System.out.print("Enter y1: ");
        int y2 = input.nextInt();

        if (x1 == x2) {
            System.out.println("The line is perpendicular to the X-axis (it's vertical).");
        } else if (y1 == y2) {
            System.out.println("The line is perpendicular to the Y-axis (it's horizontal).");
        } else {
            System.out.println("The line is not perpendicular to either axis.");
        }


    }
}
