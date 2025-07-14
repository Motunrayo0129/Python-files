public class DiamondPrintingAsterick {
    public static void main(String[] args) {
        for(int tri = 1; tri <= 5; tri++) {
            for (int angle = 1; angle <= 5 - tri; angle++) {
                System.out.print("  ");
            }
            for (int space = 1; space <= 2 * tri - 1; space++) {
                System.out.print("* ");
            }
            System.out.println();
        }
        for (int row = 5 - 1; row >= 1; row--) {
            for (int space = 1; space <= 5 - row; space++) {
                System.out.print("  ");
            }
            for (int star = 1; star <= 2 * row - 1; star++) {
                System.out.print("* ");
            }
            System.out.println();
        }

    }
}
