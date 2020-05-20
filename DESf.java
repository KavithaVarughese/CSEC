import javax.crypto.*;
import javax.crypto.spec.DESKeySpec;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.*;
import java.security.*;
import java.security.spec.AlgorithmParameterSpec;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.KeySpec;

public class DESf {
    private static Cipher encryptCipher;
    private static Cipher decryptCipher;
    //private static byte[] iv =
            //{ 0x0a, 0x01, 0x02, 0x03, 0x04, 0x0b, 0x0c, 0x0d };

    public static void main(String[] args) {
        String clearTextFile = args[0];
        String cipherTextFile = args[1];
        String clearTextNewFile = args[2];

        try {
            // create SecretKey using KeyGenerator

            KeyGenerator keyGenerator = KeyGenerator.getInstance("DES");
            SecureRandom secureRandom = new SecureRandom();
            int keyBitSize = 56;
            keyGenerator.init(keyBitSize,secureRandom);
            SecretKey key = keyGenerator.generateKey();
//            AlgorithmParameterSpec paramSpec = new IvParameterSpec(iv);

//            System.out.println(key);
//            Cipher cipher = Cipher.getInstance("DES/ECB/PKCS7Padding", "BC")

            // get Cipher instance and initiate in encrypt mode
            encryptCipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
            encryptCipher.init(Cipher.ENCRYPT_MODE, key);
            // method to encrypt clear text file to encrypted file
            encrypt(new FileInputStream(clearTextFile), new FileOutputStream(cipherTextFile));
//            System.out.println(encryptCipher.getBlockSize());
            // get Cipher instance and initiate in decrypt mode
            decryptCipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
            decryptCipher.init(Cipher.DECRYPT_MODE, key);
            //method to decrypt encrypted file to clear text file
           decrypt(new FileInputStream(cipherTextFile), new FileOutputStream(clearTextNewFile));

           
            // method to decrypt encrypted file to clear text file
            //decrypt(new FileInputStream(cipherTextFile), new FileOutputStream(clearTextNewFile));
        } catch (NoSuchAlgorithmException | NoSuchPaddingException | InvalidKeyException | IOException e) {
            e.printStackTrace();
        }

    }

    private static void encrypt(InputStream is, OutputStream os) throws IOException {
        long startTime = System.nanoTime();
        // create CipherOutputStream to encrypt the data using encryptCipher
        CipherOutputStream cos = new CipherOutputStream(os, encryptCipher);
        ///1000000;
        writeDataEncrypt(is, cos);
        long endTime = System.nanoTime();
        long totalTime = (endTime - startTime)/1000000;
        System.out.println(totalTime);
    }

    private static void decrypt(InputStream is, OutputStream os) throws IOException {

        long startTime = System.nanoTime();
        // create CipherOutputStream to decrypt the data using decryptCipher
        CipherInputStream cis = new CipherInputStream(is, decryptCipher);
       
        writeDataDecrypt(cis, os);
        long endTime = System.nanoTime();
        long totalTime = (endTime - startTime)/1000000;
        System.out.println(totalTime);
    }

    // utility method to read data from input stream and write to output stream
    private static void writeDataEncrypt(InputStream is, CipherOutputStream os) throws IOException {
        byte[] buf = new byte[8];
        int numRead = 0;
        // read and write operation
        while ((numRead = is.read(buf)) >= 0) {
            os.write(buf, 0, numRead);
        }
        os.flush();
        os.close();
        is.close();
    }
    private static void writeDataDecrypt(CipherInputStream is, OutputStream os) throws IOException {
        byte[] buf = new byte[8];
        int numRead = 0;
        // read and write operation
        while ((numRead = is.read(buf)) >= 0) {
            os.write(buf, 0, numRead);
        }
        //os.flush();
        os.close();
        is.close();
    }

}