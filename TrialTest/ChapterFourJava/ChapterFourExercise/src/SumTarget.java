import java.util.Scanner;

public class SumTarget {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the target number: ");
        int target = input.nextInt();

        int sum = 0;
        while(sum < target){
            System.out.print("Enter the number: ");
            int number = input.nextInt();
            sum = sum + number;
        }
        System.out.println("Target reached! Final sum is " + sum);
    }
}
