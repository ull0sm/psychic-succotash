import java.util.Scanner;

class palindrome{
    public static int string_length(String s){
        int n = 0 ;
        do {
            n = n+1;
        } while (s.charAt(n)!= '\0');
        return n;
    }
    public static boolean ispalindrome(String s){
        return true;
        
    }    
    public static void main(String[] args) {
        System.out.println("enter the word/number : ");
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        if (ispalindrome(word)) {
            System.out.println("your word is a palindrome");
        }
        else{
            System.out.println("nope");
        }
        System.out.println(string_length(word));
    }
}
