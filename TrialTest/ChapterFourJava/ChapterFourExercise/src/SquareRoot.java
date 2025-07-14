public class SquareRoot {
    public static double squareRoot(double number) {
        if (number % 2 == 0){
            double low = 0, high = number, mid = 0;
            double epsilon = 1e-6;

            while ((high - low) > epsilon){
                mid = (low + high) / 2;
                if (mid * mid > number){
                    high = mid;
                }
                else{
                    low = mid;
                }

            }
           return mid;
        }
        return number - 1;
    }

    public static void main(String[] args) {
        double number = 8;
        System.out.println(squareRoot(number));
    }
}
