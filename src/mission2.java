import static java.util.Collections.min;

public class mission2 {
    public static void main() {
        char[] ch = {'a', 'z', 'm', 'A'};
        char charMin = Min(ch);
        char charMax = Max(ch);
        System.out.println(charMin + " | " + charMax);

        byte[] by = {5, -1, 0, 100, -100};
        byte byteMin = Min(by);
        byte byteMax = Max(by);
        System.out.println(byteMin + " | " + byteMax);

        short[] sho = {1000, -1000, 2000, -2000};
        short shortMin = Min(sho);
        short shortMax = Max(sho);
        System.out.println(shortMin + " | " + shortMax);

        int[] in = {10, 20, 0, -5, 100};
        int intMin = Min(in);
        int intMax = Max(in);
        System.out.println(intMin + " | " + intMax);

    }
}
