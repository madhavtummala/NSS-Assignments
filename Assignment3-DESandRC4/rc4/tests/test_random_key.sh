#!/bin/bash

# We should be capable to use a urandom 256 Bytes key

# Get a urandom key
head -c 256 < /dev/urandom > tests/rkey

# Get a urandom file
head -c 2048 < /dev/urandom > tests/2048.tmp

# Cipher and decipher it, with our urandom key
./rc4 tests/rkey < tests/2048.tmp | ./rc4 tests/rkey > tests/2048.tmp.diff

# Check difference
diff tests/2048.tmp tests/2048.tmp.diff || exit 1

