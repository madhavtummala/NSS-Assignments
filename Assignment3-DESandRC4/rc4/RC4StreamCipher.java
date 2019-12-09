import java.util.*;

public class RC4StreamCipher 
{
  public static void main(String args[]) 
  {
    //Create a cipher object
    RC4StreamCipher obj = new RC4StreamCipher();
    //Get the 256 bit key in cipherblock array
    int cipherblock[] = obj.KeySchedulingALgorithm("Key");
    //Make a copy so that decryption can be done later
    int copy[] = Arrays.copyOf(cipherblock, cipherblock.length);
    //Encrypt with the Pseudo random generator algorithm
    String ciphertext = obj.PRGAAlgorithmEncrypt("Plaintext", cipherblock);
    System.out.println("Ciphertext is: "+ciphertext);
    //Decrypt and check
    String plaintext = obj.PRGAAlgorithmDecrypt(ciphertext, copy);
    System.out.println("Plaintext is: "+plaintext);
    //Follow the same procedure for the next key
    int cipherblock2[] = obj.KeySchedulingALgorithm("key");
    int copy2[] = Arrays.copyOf(cipherblock2, cipherblock2.length);
    ciphertext = obj.PRGAAlgorithmEncrypt("Plaintext", cipherblock2);
    System.out.println("Ciphertext is: "+ciphertext);
    plaintext = obj.PRGAAlgorithmDecrypt(ciphertext, copy2);
    System.out.println("Plaintext is: "+plaintext);
  }
  /* Note, we can use the same algorithm for encryption and decryption,
  and that's how it is done in real world. I have broken it into two functions
  to enhance readability, but the main loop in both is same
  */
  public int[] KeySchedulingALgorithm(String key) 
  {
    int l= key.length(), i, j=0;
    //key=key.toLowerCase();
    int arr[] = new int [256];
    for (i = 0; i < 256; i++)
    {
      arr[i] = i;
    }
    for (i=0;i<256;i++)
    {
      char c = key.charAt(i%l);
      j = (j+arr[i]+c)%256;
      int temp = arr[i];
      arr[i]=arr[j];
      arr[j]=temp;
    }
    return arr;
  }
  public String PRGAAlgorithmEncrypt(String plaintext, int arr[])
  {
    int i=0,l=plaintext.length(),j=0,k=0,res;
    String str="";
    for(k=0;k<l;k++)
    {
      i = (i+1)%256;
      j = (j+arr[i])%256;
      int temp = arr[i];
      arr[i]=arr[j];
      arr[j]=temp;
      res=arr[(arr[i]+arr[j])%256];
      String s = Integer.toHexString(res^plaintext.charAt(k));
      if (s.length()<2)
        s= "0"+s;
      str+=s;
    }
    return str;
  }
  public String PRGAAlgorithmDecrypt(String ciphertext, int arr[])
  {
    int i=0,l=ciphertext.length(),j=0,k=0,res;
    String str="";
    for(k=0;k<l;k+=2)
    {
      i = (i+1)%256;
      j = (j+arr[i])%256;
      int temp = arr[i];
      arr[i]=arr[j];
      arr[j]=temp;
      res=arr[(arr[i]+arr[j])%256];
      String hex= ciphertext.charAt(k)+"";
      hex += ciphertext.charAt(k+1);
      int x=Integer.parseInt(hex,16)^res;
      str+=(char)x;
    }
    return str;
  }
}
