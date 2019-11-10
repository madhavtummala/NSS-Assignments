#!/bin/bash

# We could cipher one byte text

# Get two keys. One key is 256 bytes lenght, and the other one is 1 byte length
head -c 256 < /dev/urandom > tests/key_256.tmp
head -c 1 < /dev/urandom > tests/key_1b.tmp

# Get one byte file
head -c 1 < /dev/urandom > tests/one_byte.tmp

# Cipher and decipher
./rc4 tests/key_256.tmp < tests/one_byte.tmp | ./rc4 tests/key_256.tmp > tests/one_byte.tmp.diff
./rc4 tests/key_1b.tmp < tests/one_byte.tmp | ./rc4 tests/key_1b.tmp > tests/one_byte_key_and_text.tmp.diff

# Check difference
diff tests/one_byte.tmp tests/one_byte.tmp.diff || exit 1
diff tests/one_byte.tmp tests/one_byte_key_and_text.tmp.diff || exit 1 
