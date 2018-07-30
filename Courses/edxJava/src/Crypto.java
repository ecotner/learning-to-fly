public class Crypto {
    public static void main (String[] args) {
        String plaintext = "Hello world!";
        int key = 10;
        String cipher_text = groupify(caeserify(normalizeText(plaintext), key), 2);
        String decrypted_text = decrypt(cipher_text, key);
        System.out.println(plaintext);
        System.out.println(cipher_text);
        System.out.println(decrypted_text);
    }

    public static String normalizeText(String text) {
        text = text.replaceAll("[[0-9][^a-zA-Z][\\s]]", "").toUpperCase();
        return text;
    }

    public static String caeserify(String text, int key) {
        /** Creates a ciphertext using the Caeser cipher. Assumes plaintext is all uppercase and has no whitespace.
         * @text: the plaintext to encrypt
         * @key: an integer by which the alphabet is shifted */
        // Create a StringBuilder to construc the cipher
        StringBuilder stringBuilder = new StringBuilder(text.length());
        char temp_char = 'A';
        int temp_char_int = 0;
        // Iterate over every character in the plaintext
        for (int i = 0; i < text.length(); i++) {
            // Extract the character from the plaintext, convert to int, shift, then convert back to character
            temp_char = text.charAt(i);
            temp_char_int = (int) temp_char + key;
            if (temp_char_int < 65) temp_char_int += 26;
            else if (temp_char_int > 90) temp_char_int -= 26;
            temp_char = (char) temp_char_int;
            // Append to stringBuilder
            stringBuilder.append(temp_char);
        }
        return stringBuilder.toString();
    }

    public static String groupify(String text, int size) {
        // Create StringBuilder
        StringBuilder stringBuilder = new StringBuilder(text.length() * 2);
        stringBuilder.append(text.charAt(0));
        // Iterate through characters in text
        for (int i=1; i < text.length(); i++) {
            // Every time i%size==0, insert whitespace before appending
            if (i % size == 0) stringBuilder.append(' ');
            stringBuilder.append(text.charAt(i));
        }
        return stringBuilder.toString();
    }

    public static String decrypt(String ciphertext, int key) {
        /** Decrypts the Caeser cipher. Basically just uses the cipher backwards (with key -> -key). */
        // Eliminates whitespace
        ciphertext = ciphertext.replaceAll("\\s", "");
        // Undoes the cipher
        return caeserify(ciphertext, -key);
    }
}
