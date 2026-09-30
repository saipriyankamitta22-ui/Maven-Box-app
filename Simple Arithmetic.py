import java.util.Scanner; // Import the Scanner class to read user input

public class AddNumbers {
    public static void main(String[] args) {
        // Create a Scanner object to read text from the standard input (keyboard)
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter the first number: ");
        int num1 = input.nextInt(); // Reads the first integer
        
        System.out.print("Enter the second number: ");
        int num2 = input.nextInt(); // Reads the second integer
        
        // Calculate the sum
        int sum = num1 + num2;
        
        // Print the result
        System.out.println("The sum of " + num1 + " and " + num2 + " is: " + sum);
        
        input.close(); // Close the scanner resource
    }
}
