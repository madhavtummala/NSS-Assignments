#!/bin/bash

# This program only reads the first 256 Bytes of the key file.
# So if we put a larger key file, it's equivalent to a "head -c 256" of that file.

# Get a long key and the fist 512 and 256 bytes of it
head -c 2048 < /dev/urandom > tests/long.tmp
head -c 512 < tests/long.tmp > tests/medium.tmp
head -c 256 < tests/long.tmp > tests/max.tmp

# Get a test file
head -c 2048 < /dev/urandom > tests/file.tmp

# cipher and decipher
./rc4 tests/long.tmp < tests/file.tmp | ./rc4 tests/medium.tmp > tests/file_med.tmp.diff
./rc4 tests/long.tmp < tests/file.tmp | ./rc4 tests/max.tmp > tests/file_max.tmp.diff
./rc4 tests/medium.tmp < tests/file.tmp | ./rc4 tests/max.tmp > tests/file_mm.tmp.diff

# Check difference
diff tests/file.tmp tests/file_med.tmp.diff || exit 1
diff tests/file.tmp tests/file_max.tmp.diff || exit 1
diff tests/file.tmp tests/file_mm.tmp.diff || exit 1
