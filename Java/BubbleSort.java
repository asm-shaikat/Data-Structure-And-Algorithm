import java.util.Scanner;

public class BubbleSort {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter array size");
        int arySize = scn.nextInt();
        int[] ary = new int[arySize];

        System.out.println("Enter array elements");
        for (int i = 0; i < arySize; i++) {
            ary[i] = scn.nextInt();
        }
        sub(ary);
    }

    public static void sub(int[] ary) {
        for (int i = 0; i < ary.length; i++) {
            for (int j = 0; j < ary.length - i - 1; j++) {
                if (ary[j] > ary[j + 1]) {
                    int temp = ary[j + 1];
                    ary[j + 1] = ary[j];
                    ary[j] = temp;
                }
            }
        }
        System.out.println("Sorted array");
        for (int k = 0; k < ary.length; k++) {
            System.out.print(ary[k] + " ");
        }
    }

}