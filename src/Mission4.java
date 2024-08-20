import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Mission4 {

    public static List<String> corsina;

    static {
        corsina = new ArrayList<>();
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        System.out.print("Введите строку: ");
        String input = scan.nextLine();
        corsina.add(input);

        System.out.println (corsina);
    }
}
