import java.util.Scanner;
import java.util.Random;

public class OddsOrEvens {
    public static void main (String[] args) {
        System.out.println("Let's play a game called \"Odds and Evens\"");
        System.out.print("What is your name? ");
        Scanner input = new Scanner(System.in);
        String name = input.nextLine();
        System.out.print("Hi " + name + ", which do you choose? (O)dds or (E)vens? ");
        String oddsOrEvens = input.next();
        if (oddsOrEvens.equals("O")) {
            System.out.println(name + " has picked odds! The computer will be evens.");
        } else {
            System.out.println(name + " has picked evens! The computer will be odds.");
        }
        System.out.println("----------------------------------------------------------");

        System.out.print("How many \"fingers\" do you want to put out? ");
        int n_fingers = input.nextInt();
        Random rand = new Random();
        int computer = rand.nextInt(6);
        System.out.println("The computer plays " + computer + " \"fingers\".");
        System.out.println("----------------------------------------------------------");

        int sum = n_fingers + computer;
        System.out.println(Integer.toString(n_fingers) + " + " + Integer.toString(computer) + " = " + Integer.toString(sum));
        boolean isEven = (sum % 2 == 0);
        if (isEven) {
            System.out.println(Integer.toString(sum) + " is... even!");
        } else {
            System.out.println(Integer.toString(sum) + " is... odd!");
        }
        if ((isEven && oddsOrEvens.equals("E")) || (!isEven && oddsOrEvens.equals("O"))) {
            System.out.println("That means " + name + " wins! :)");
        } else {
            System.out.println("That means the computer wins... sorry. :(");
        }
        System.out.println("----------------------------------------------------------");
    }
}
