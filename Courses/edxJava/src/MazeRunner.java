import java.util.*;

public class MazeRunner {
    public static Maze myMap = new Maze();
    public static Scanner input = new Scanner(System.in);

    public static void main(String[] args){
        intro();
        String user_move = "";
        while (!myMap.didIWin()){
            user_move = userMove();
            actualMove(user_move);
            myMap.printMap();
        }
        System.out.println("Congrats, you made it out alive!");
    }

    public static void intro(){
        System.out.println("Welcome to Maze Runner!");
        System.out.println("Here is your current position:");
        myMap.printMap();
    }

    public static String userMove(){
        Set<String> options = new HashSet<>();
        options.addAll(Arrays.asList("R", "L", "U", "D"));
        String response = "";
        boolean valid_input = false;
        while (!valid_input) {
            System.out.print("Where would you like to move? (R, L, U, D) ");
            response = input.nextLine();
            // Sanitize input to make sure it's one of the chosen options
            response = response.toUpperCase();
            if (options.contains(response)){
                valid_input = true;
            } else {
                System.out.println("Sorry, incorrect input.");
            }
        }
        return response;
    }

    public static void actualMove(String user_move){
        // check for pits
        if (myMap.isThereAPit(user_move)){
            // ask if player wants to jump the pit
            System.out.print("Watch out, there's a pit ahead! Jump it? ");
            String response = input.next();
            response = response.toUpperCase();
            // if so, jump the pit
            if (response.equals("Y")){
                myMap.jumpOverPit(user_move);
            }
        }
        // perform normal moves in cardinal directions
        else if (user_move.equals("R")){
            if (myMap.canIMoveRight()){
                myMap.moveRight();
            } else {
                System.out.println("Sorry, you've hit a wall.");
            }
        }
        else if (user_move.equals("L")){
            if (myMap.canIMoveLeft()){
                myMap.moveLeft();
            } else {
                System.out.println("Sorry, you've hit a wall.");
            }
        }
        else if (user_move.equals("U")){
            if (myMap.canIMoveUp()){
                myMap.moveUp();
            } else {
                System.out.println("Sorry, you've hit a wall.");
            }
        }
        else if (user_move.equals("D")){
            if (myMap.canIMoveDown()){
                myMap.moveDown();
            } else {
                System.out.println("Sorry, you've hit a wall.");
            }
        }
    }
}
