import java.util.Scanner;

public class LearnScanner {
    public static void main(String[] args){
        askName();
        askAge();
    }

    public static void askName() {
        Scanner input = new Scanner(System.in);
        System.out.println("Hello, what's your name?");
        String name = input.next();
        System.out.println("Nice to meet you, " + name);
    }

    public static void askAge() {
        Scanner input = new Scanner(System.in);
        System.out.println("How old are you?");
        int age = input.nextInt();
        System.out.println("So, you're " + age + " years old!");
    }
}
