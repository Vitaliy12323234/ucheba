import java.util.Scanner;

public class mission5 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Придумайте пароль: ");
        String password = scan.nextLine();
        String ent;
        boolean i = false;
        while (!i) {
            System.out.print("Введите пароль: ");
            ent = scan.nextLine();

            if (ent.equals(password)) {
                System.out.println("Пароль верный");
                i = true;
            } else {
                System.out.println("Пароль неверный, попробуйте снова");
            }
        }

        scan.close();
    }
}
