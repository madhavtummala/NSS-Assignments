# RC4 Implementation

Name: T.Madhav
RollNo: 16CS01041
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