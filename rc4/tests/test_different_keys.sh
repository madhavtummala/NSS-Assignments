#!/bin/bash

# We shouldn't be able to decipher a file with a different key.

# Get two 256 Bytes keys
head -c 256 < /dev/urandom > tests/key0.tmp
head -c 256 < /dev/urandom > tests/key1.tmp


# Get a test file
head -c 4096 < /dev/urandom > tests/test.tmp

# Cipher it
./rc4 tests/key0.tmp < tests/test.tmp | ./rc4 tests/key1.tmp > tests/test.tmp.diff

# These should be different files
diff tests/test.tmp tests/test.tmp.diff > /dev/null

if [ "$?" = "0" ]
then
    exit 1
fi
