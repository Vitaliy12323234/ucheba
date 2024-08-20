import java.util.Scanner;

public class mission1  {
    public static void main () {
        int a;
        int b;
        Scanner scan = new Scanner(System.in);
        a = scan.nextInt();
        Scanner nescan = new Scanner(System.in);
        b = nescan.nextInt();
        if(a > b)
            System.out.println(a);
        if(a < b)
            System.out.println(b);
        if(a == b)
            System.out.println("Они ровны");
    }
}

