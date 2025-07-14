public class Factorial {
    public static void main(String[] args) {
        int number = 5;
        int factorial = 1;

        for(int num = 1; num <= 5; num++){
            factorial = factorial * num;
        }
        System.out.printf("The factorial of %d is: %d%n", number, factorial);

    }
}
