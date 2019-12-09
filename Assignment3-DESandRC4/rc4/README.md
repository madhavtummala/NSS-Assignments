# RC4 Implementation

Name: T.Madhav & Aditya Pal  
RollNo: 16CS01041 & 16CS01017  
Course: NSS

## Creating a key

You will need to a key to use in encryption (less than 256 bytes).  
Here is a way to generate a random key (128 bytes long).  

```
head -c 128 < /dev/urandom > my.key
chmod 400 my.key
```

## Running the code

Entire code is written in `rc4.c`.
The ascii input is taken through stdin, ascii output through stdout and hex ouput through stderr.

```
gcc main.c rc4.c -o rc4
./rc4 <your_key_file>											
```
example:
```
echo -n "not so obvious" > my.key       						# my secret key
echo -n "this is a secret" | ./rc4 my.key > message.rc4       	# encrypted message
cat message.rc4 | ./rc4 my.key 									# decrypted message
```

## Analysis

To show that this implementation of rc4 working properly for various key sizes and message sizes, I have written a bash script to perform some tests.
```
./tests/run_tests.sh
```

Basically this is the main script that calls other scripts named `test_*.sh` in `tests/` and runs them. Tests vary the key and message size and test if the algorithm is still working.   
Each test creates random key and random message using `/dev/urandom`, then it ciphers and deciphers the message to check if the deciphered message is same as the original message. If it is same, then the test has passed. 
And finally we also check with the example given in wikipedia for rc4.  

After running the tests, clean the temporary files
```
rm -vf tests/*.tmp tests/*.diff
```

## Java Version (Added by [PalAditya](https://github.com/PalAditya))

The Java version is far less flexible than the C Version, but is added so that it might help someone out. An example output from the code is (Note: Here input is to be given as 16 hexadecimal characters, that is between 0-F and not as 8 ASCII characters):

<div style ="text-align:center"><img src="RC4.png" style="height:80px;width:300px;"></img></div>

**Note**:The number of positions in which they differ is **17**, an incredible amount considering they are only **18** nibbles long (in hexadecimal notation), making the total difference **94.4%**. Going to binary (bitwise) notation, the difference is **40** bits out of **72** bits (**55.56%**), close to the statistical value of **50%**, proving the security of RC4 ciphers. Also, since it is a stream cipher, we don’t have the problem of creating a huge key for a huge text, but can still emulate OTP like behaviour. It is also more malleable than common block ciphers.

However, there are still issues. Unlike a modern stream cipher, RC4 does not take a separate nonce alongside the key. This means that if a single long-term key is to be used to securely encrypt multiple streams, the protocol must specify how to combine the nonce and the long-term key to generate the stream key for RC4. One approach to addressing this is to generate a *fresh* RC4 key by hashing a long-term key with a nonce. However, many applications that use RC4 simply concatenate key and nonce; RC4's weak key schedule then gives rise to related key attacks like the **Fluhrer, Martin and Shamir** attack.