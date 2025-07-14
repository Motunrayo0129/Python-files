public class SumTheOdd {
    public static void main(String[] args) {
        int sum = 0;
        for (int odd = 1; odd <= 100; odd += 2) {
                sum += odd;

        }
        System.out.println("The sum odd number from 1 to 100 "
                + sum);

        int num = 1;
        while(num <= 20) {
            System.out.print(num);

            if (num % 5 == 0) {
                System.out.println();
            } else {
                System.out.print('\t');
            }
            num++;

        }
        System.out.println("\n using for loop");
        for(int nums = 1; nums <= 20; nums++) {
            System.out.print(nums);

            if (nums % 5 == 0) {
                System.out.println();
            }
            else{
                System.out.print('\t');
            }
        }

    }
}
