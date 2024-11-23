import java.util.Scanner;

class palindrome {
    //this function is used to give the length of the string in terms of integer datatype
    public static int string_length(String s) {
        int n = 0; // this is the counter variable
        for (int i = 0; ; i++) { // iteration goes upto infinite although i could i have used while loop but this found was way more simple for me
            try { //we are using try cuz it's an infinte loop
                s.charAt(i);
                n++; //when no error this counter variable is incremented
            } catch (IndexOutOfBoundsException e) { //the exception will be caught here and will break the code later
                break;
            }
        }
        return n; // here we return the final counter value
    }

    //this function is used to give true or false for the condition
    public static boolean ispalindrome(String s,int n) {
        for (int i = 0; i <= n/2; i++) { //here we go till the half of the string  
            if (s.charAt(i) != s.charAt(n-i-1)) { // half string is cuz we will be comparing the first and last soo middle we will have to stop
                return false; // if it's found last char and first char do not match then false will be returned and exited
            }
        }
        return true;

    }

    //this is the main function here all the process starts
    public static void main(String[] args) {
        //input is taken here
        System.out.println("enter the word/number : ");
        Scanner sc = new Scanner(System.in);
        String word = sc.next();

        //here we capture the length of the string so that i dont need to call string_lenght function every time
        int strlen = string_length(word);

        //here it checks the condition whether the function returns true or false according to that it will respond
        if (ispalindrome(word,strlen)) {
            System.out.println("your word is a palindrome");
        } else {
            System.out.println("nope");
        }
    }
}
