public class IntegerDivisibleBy3 {
    public static void main(String[] args) {
        int sum = 0;
        for(int nums = 1; nums <= 30; nums++) {
            if (nums % 3 == 0) {
                sum += nums;
            }
        }
        System.out.println(sum);
    }
}
