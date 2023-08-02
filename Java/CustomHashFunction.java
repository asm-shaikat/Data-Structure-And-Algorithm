public class CustomHashFunction {
    public static void main(String[] args) {
        String input = "Shaikat";
        int hashValue = customHash(input);
        System.out.println("Hash value for '" + input + "': " + hashValue);
    }

    public static int customHash(String str) {
        int hash = 0;
        // Simple hash calculation based on ASCII values
        for (int i = 0; i < str.length(); i++) {
            hash += str.charAt(i);
        }

        return hash;
    }
}
