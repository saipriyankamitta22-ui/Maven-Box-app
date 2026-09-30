public class EvenOddLoop {
    public static void main(String[] args) {
        System.out.println("Evaluating numbers from 1 to 5:");
        
        // Loop from 1 to 5
        for (int i = 1; i <= 5; i++) {
            // Check if the number is divisible by 2
            if (i % 2 == 0) {
                System.out.println(i + " is Even");
            } else {
                System.out.println(i + " is Odd");
            }
        }
    }
}
