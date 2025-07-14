public class TabularOutput {
    public static void main(String[] args){

        System.out.printf("%-5s %-5s %-5s %-5s%n", "N", "N2", "N3", "N4");
        for (int n = 1; n <= 5; n++) {
            int n2 = n * n;
            int n3 = n2 * n;
            int n4 = n3 * n;
            System.out.printf("%-5d %-5d %-5d %-5d%n", n, n2, n3, n4);
        }

    }
}
