import java.util.Scanner;

public class ValidatingInput {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);


        System.out.print("Please enter a number of students: ");
        int students = input.nextInt();
        int failures = 0;
        int passes = 0;
        for (int num = 1; num <= students; num++) {
            System.out.print("Please enter a student grade '1' for pass '2' for fail: ");
            int grade = input.nextInt();
            while (grade != 1 && grade != 2) {
                System.out.print("Enter a grade between 1 and 2: ");
                grade = input.nextInt();
            }
                if (grade == 1) {
                    passes += 1;
                } else if (grade == 2) {
                    failures += 1;
                }
        }


            System.out.println("The number of student passes is: " + passes);
            System.out.println("The number of student failures is: " + failures);



    }
}
