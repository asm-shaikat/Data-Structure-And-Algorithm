import java.util.Scanner;
import java.util.Vector;

public class InsertionSort {
    public static void main(String[] args) {
        System.out.println("Enter array size: ");
        Scanner scanner = new Scanner(System.in);
        int arySize = scanner.nextInt();
        Vector<Integer> vec = new Vector<Integer>();

        System.out.println("Enter array element:");
        for (int i = 0; i < arySize; i++) {
            int a = scanner.nextInt();
            vec.add(a);
        }

        for (int i = 1; i < vec.size(); i++) {
            int check = vec.get(i);
            int j = i - 1;
            while (j >= 0 && vec.get(j) > check) {
                vec.set(j + 1, vec.get(j));
                j = j - 1;
            }
            vec.set(j + 1, check);
        }

        System.out.println("Sorted Array: ");
        for (Integer element : vec) {
            System.out.print(element + " ");
        }

    }
}
