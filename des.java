import javax.crypto.*;
import javax.crypto.spec.IvParameterSpec;
import java.io.*;
import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.security.spec.AlgorithmParameterSpec;

public class des {
    private static Cipher encryptCipher;
    private static Cipher decryptCipher;
    private static final byte[] iv = { 11, 22, 33, 44, 99, 88, 77, 66 };

    public static void main(String[] args) {
        String clearTextFile = args[0];
        String cipherTextFile = args[1];
        String clearTextNewFile = args[2];
        //String clearTextNewFile = "/Users/pankaj/source-new.txt";

        try {
            // create SecretKey using KeyGenerator
            SecretKey key = KeyGenerator.getInstance("DES").generateKey();
            AlgorithmParameterSpec paramSpec = new IvParameterSpec(iv);

            // get Cipher instance and initiate in encrypt mode
            encryptCipher = Cipher.getInstance("DES/CBC/PKCS5Padding");
            encryptCipher.init(Cipher.ENCRYPT_MODE, key, paramSpec);
            // method to encrypt clear text file to encrypted file
            encrypt(new FileInputStream(clearTextFile), new FileOutputStream(cipherTextFile));

            // get Cipher instance and initiate in decrypt mode
            decryptCipher = Cipher.getInstance("DES/CBC/PKCS5Padding");
            decryptCipher.init(Cipher.DECRYPT_MODE, key, paramSpec);
            //method to decrypt encrypted file to clear text file
            decrypt(new FileInputStream(cipherTextFile), new FileOutputStream(clearTextNewFile));



            // method to decrypt encrypted file to clear text file
            //decrypt(new FileInputStream(cipherTextFile), new FileOutputStream(clearTextNewFile));
        } catch (NoSuchAlgorithmException | NoSuchPaddingException | InvalidKeyException
                | InvalidAlgorithmParameterException | IOException e) {
            e.printStackTrace();
        }

    }

    private static void encrypt(InputStream is, OutputStream os) throws IOException {
        long startTime = System.nanoTime();
        // create CipherOutputStream to encrypt the data using encryptCipher
        os = new CipherOutputStream(os, encryptCipher);
        long endTime = System.nanoTime();
        long totalTime = endTime - startTime;
        writeData(is, os);
        System.out.println(totalTime);
    }

    private static void decrypt(InputStream is, OutputStream os) throws IOException {

        long startTime = System.nanoTime();
        // create CipherOutputStream to decrypt the data using decryptCipher
        is = new CipherInputStream(is, decryptCipher);
        long endTime = System.nanoTime();
        long totalTime = endTime - startTime;
        writeData(is, os);
        System.out.println(totalTime);
    }

    // utility method to read data from input stream and write to output stream
    private static void writeData(InputStream is, OutputStream os) throws IOException {
        byte[] buf = new byte[1024];
        int numRead = 0;
        // read and write operation
        while ((numRead = is.read(buf)) >= 0) {
            os.write(buf, 0, numRead);
        }
        os.close();
        is.close();
    }

}