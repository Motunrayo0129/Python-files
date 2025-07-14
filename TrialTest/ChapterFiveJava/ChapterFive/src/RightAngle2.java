public class RightAngle2 {
    public static void main(String[] args) {
        for (int row = 1; row <= 10; row++) {
            for (int a = 1; a <= row; a++) {
                System.out.print('*');
            }

            System.out.print("  ");

            for (int b = 1; b <= 11 - row; b++) {
                System.out.print('*');
            }

            System.out.print("  ");

            for (int c = 1; c <= 11 - row; c++) {
                System.out.print('*');
            }

            System.out.print("  ");

            for (int d = 1; d <= row; d++) {
                System.out.print('*');
            }

            System.out.println();
        }

    }
}
