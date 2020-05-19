import java.lang.*;
import java.io.*;
import java.io.FileInputStream;
import java.io.FileOutputStream;

import javax.crypto.*;
import javax.crypto.spec.SecretKeySpec;

class Blowfish
{

    private static Cipher encryptCipher;
    private static Cipher decryptCipher;

    public static void main(String[] args) throws Exception {
        String clearTextFile = args[0];
        String cipherTextFile = args[1];
        String clearTextNewFile = args[2];

        String keytext = "mykey";
        SecretKey secret_key = new SecretKeySpec(keytext.getBytes(), "Blowfish");

        encryptCipher = Cipher.getInstance("Blowfish/ECB/PKCS5Padding");
        encryptCipher.init(Cipher.ENCRYPT_MODE, secret_key);
        blowfishEncrypt(new FileInputStream(clearTextFile), new FileOutputStream(cipherTextFile));

        decryptCipher = Cipher.getInstance("Blowfish/ECB/PKCS5Padding");
        decryptCipher.init(Cipher.DECRYPT_MODE, secret_key);
        blowfishDecrypt(new FileInputStream(cipherTextFile) , new FileOutputStream(clearTextNewFile));

    }

    public static void blowfishEncrypt(InputStream is, OutputStream os) throws IOException {

        long startTime = System.nanoTime();
        // create CipherOutputStream to encrypt the data using encryptCipher
        os = new CipherOutputStream(os, encryptCipher);
        long endTime = System.nanoTime();
        long totalTime = endTime - startTime;
        writeData(is, os);
        System.out.println(totalTime);

    }
    public static void blowfishDecrypt(InputStream is, OutputStream os) throws IOException {

        long startTime = System.nanoTime();
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