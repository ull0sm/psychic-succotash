import java.util.Scanner;
//future upgrade can be doing islarge and issmall in one function itself
class LargestSmallestNum{
    public static int islarge(int[] n){
        int large=n[0];
        for (int i = 1; i < 3; i++) {
            if(large<n[i]){
                large = n[i];
            }
        }
        return large;
    }
    public static int issmall(int[] n){
        int small=n[0];
        for (int i = 1; i < 3; i++) {
            if(small>n[i]){
                small = n[i];
            }
        }
        return small;
    }

    public static void main(String[] args){
        System.out.println("enter the three number:");
        Scanner sc = new Scanner(System.in);

        int[] num = new int[3];
        for (int i = 0; i < 3; i++) {
            num[i] = sc.nextInt();
        }
        int largest = islarge(num);
        int smallest = issmall(num);

        System.out.println(largest);
        System.out.println(smallest);
       
    }
}