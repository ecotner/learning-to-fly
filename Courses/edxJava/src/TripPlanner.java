import java.util.Scanner;
import java.lang.Math;

public class TripPlanner {
    public static /*final*/ String stars = "**********";
    public static void main(String[] args) {
        greeting();
        timeAndBudget();
        timeDifference();
        countryArea();
        distance();
    }

    public static void greeting() {
        Scanner input = new Scanner(System.in);
        System.out.print("Hello, what's your name? ");
        String name = input.nextLine();
        System.out.print("Nice to meet you, " + name + ", where are travelling to? ");
        String destination = input.nextLine();
        System.out.println("Great! " + destination + " sounds like a great trip.");
        System.out.println(stars);
        System.out.println();
    }

    public static void timeAndBudget() {
        Scanner input = new Scanner(System.in);

        // Get information
        System.out.print("How many days are you going to spend travelling? ");
        int days = input.nextInt();
        System.out.print("How much money, in USD, are you planning to spend on your trip? ");
        int money = input.nextInt();
        System.out.print("What is the three-letter currency symbol for your travel destination? ");
        String currency_symbol = input.next();
        System.out.println("How many " + currency_symbol + " are there in 1 USD? ");
        double conversion = input.nextDouble();
        System.out.println();

        // Convert time and currency
        int hours = days * 24;
        int minutes = hours * 60;
        System.out.println("If you are travelling for "
                + days + " days, that is  the same as " + hours
                +" hours or " + minutes + " minutes.");

        double daily_budget = money/days;
        System.out.println("If you are going to spend $" + money
                + " USD, that means you can spend $" + daily_budget
                + " per day.");
        double total = conversion * money;
        System.out.println("Your total budget in " + currency_symbol + " is "
                + total + ", which is " + (total/days) + " "
                + currency_symbol + " per day.");
        System.out.println(stars);
        System.out.println();
    }

    public static void timeDifference() {
        Scanner input = new Scanner(System.in);
        System.out.print("What is the time difference, in hours, between your home and destination? ");
        int time_diff = input.nextInt();
        int midnight_time;
        int noon_time;
        if(time_diff < 0) {
            midnight_time = 24 + time_diff;
        } else {
            midnight_time = time_diff;
        }
        noon_time = 12 + time_diff;
        System.out.println("That means that when it is midnight at home it will be "
                + midnight_time + ":00 at your travel destination, and when it is noon at home, it will be "
                + noon_time + ":00.");
        System.out.println(stars);
        System.out.println();
    }

    public static void countryArea() {
        Scanner input = new Scanner(System.in);
        System.out.print("What is the square area of your destination country in km2 ");
        double km2 = input.nextDouble();
        double mi2 = km2/ (1.6*1.6);
        System.out.println("In mi2 that is " + mi2 + ".");
        System.out.println(stars);
        System.out.println();
    }

    public static void distance() {
        double PI = 3.141592654;
        Scanner input = new Scanner(System.in);

        // Get location information from the user
        System.out.print("What is the longitude of the destination? ");
        double dest_longitude = input.nextDouble();
        System.out.print("What is the latitude of the destination? ");
        double dest_latitude = input.nextDouble();
        System.out.print("What is your home longitude? ");
        double home_longitude = input.nextDouble();
        System.out.print("What is your home latitude? ");
        double home_latitude = input.nextDouble();

        // Convert degrees to radians
        double deg_to_rad = PI/180;
        dest_latitude *= deg_to_rad;
        dest_longitude *= deg_to_rad;
        home_latitude *= deg_to_rad;
        home_longitude *= deg_to_rad;

        // Calculate distance in km
        double r = 6300;
        double x2 = Math.pow(Math.sin((dest_latitude - dest_latitude)/2), 2);
        double y2 = Math.cos(home_latitude) * Math.cos(dest_latitude) * Math.pow((dest_longitude - home_longitude)/2, 2);
        double dist = 2*r*Math.asin(Math.sqrt(x2 + y2));
        System.out.println("Distance between home and destination is "
                + dist + " km.");
    }
}
