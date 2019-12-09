# DES Implementation

Name: T.Madhav & Aditya Pal  
RollNo: 16CS01041 & 16CS01017  
Course: NSS

## Setting the key and message

You will be asked for key and message input.  
Give strictly 8-character (ascii) key and message input.  
The keys modifications after IP, rounds, the encrypted and decrypted messages will be printed.  

example:
```
Enter Key:
2736CCDD
Enter Message:
Hi
32  37  33  36  43  43  44  44
48  69  00  00  00  00  00  00
Round Key 1: 20 38 44 77 20 D5
Round Key 2: 00 34 54 E2 A2 C7
Round Key 3: 44 44 54 76 A7 8B
Round Key 4: 46 C1 20 3E 15 4B
Round Key 5: 8A 81 23 4E F1 62
Round Key 6: A9 02 0B 64 ED 68
Round Key 7: 21 12 88 E8 9C 5A
Round Key 8: 10 18 D0 CD D6 3A
Round Key 9: 10 48 50 89 DF 28
Round Key 10: 04 69 14 58 5E 34
Round Key 11: 06 25 05 D9 48 BC
Round Key 12: 4B 04 21 81 7A 99
Round Key 13: C9 80 A8 B3 32 35
Round Key 14: 90 82 8A B3 0B A6
Round Key 15: 30 1A 02 14 2B 97
Round Key 16: 30 3A 00 B4 21 C5

Encrypted: BF B3 EB 4E 93 F4 ED 0E

Decrypted: Hi
```

## Running the code

```bash
gcc des.c -o des
./des
```
## Analysis

The implementation has been done with analysis in mind. Every aspect of this DES implementation is customizable. It is especially designed to test attacks against DES by allowing to change practically all aspects of the algorithm:
* Number of rounds (from 0 to 16)
* Enable/Disable permutations (permutation P, initial permutation (IP) and final permutation (FP))
* Allow 56bit and 64bit keys
* Enable/Disable parity check for key
* Provide custom SBOXes, IP table, FP table, expansion table, permutation table, Permuted Choice 1, Permuted Choice 2 and key shifts

At first, the algorithm has to be configured using a ```DES_Config``` structure. It is advisable to copy the ```DES_default``` config and modify the copy. 

A simple example to disable the initial and final permutations (IP and FP) and reduce the number of rounds to 4 would be
```C
DES_Config cfg = DES_default;
cfg.iperm = 0; // disable initial permutation
cfg.fperm = 0; // disable final permutation
cfg.rounds = 4; // reduce to 4 rounds
```


## Java Version (Added by [PalAditya](https://github.com/PalAditya))

The Java version is far less flexible than the C Version, but is added so that it might help someone out. An example output from the code is (Note: Here input is to be given as 16 hexadecimal characters, that is between 0-F and not as 8 ASCII characters):

<img src="DES.png" style="height:320px;width:850px;align:center"></img>

**Note**: Difference in hexadecimal *nibbles* is **90/96**, or **93.75%** and in binary (bitwise) notation, **180/384** bits or **46.875%** bits are different, again close to the statistical value of 50%. This shows the strength of DES. 

**Strength**: Strong confusion and diffusion properties, primarily due to the S-boxes (Substitution boxes). Also, encryption and decryption use the same keys (it is a *Feistel* cipher) and the same function, making it hardware friendly and cost effective. It also has the completeness property, that is each bit of ciphertext depends upon multiple bits of plaintext.
