import java.util.Scanner;

public class mission3 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.print("минимальное число: ");
        int min = scan.nextInt();

        System.out.print("максимальное число: ");
        int max = scan.nextInt();

        System.out.println("числа");
        for (int i = min; i <= max; i++) {
             System.out.println(i);
        }
        }
    }
