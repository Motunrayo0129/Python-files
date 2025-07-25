public class CompoundInterest {
    public static void main(String[] args) {
        double principal = 1000.0;
        double rate = 0.5;
        System.out.printf("%s%20s%n", "Year", "Amount on deposit");
        for(int year = 5; year <= 10; year++) {
            double amount = principal * Math.pow(1 + rate, year);
            System.out.printf("%4d%,20.2f%n", year, amount);
        }
    }
}
