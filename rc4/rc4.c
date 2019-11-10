#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>

#define BUFFER_SIZE 256
#define STDIN 0
#define STDOUT 1

typedef unsigned char Byte;

unsigned short int key_length;
Byte Key[256];
Byte S[256];
Byte i;
Byte j;

void swap(Byte i, Byte j) {
    Byte tmp = S[i];
    S[i] = S[j];
    S[j] = tmp;
}

void ksa() {
    i = 0;
    do {
        S[i] = i;
        i++;
    } while (i);
    do {
        j = j + Key[i % key_length] + S[i];
        swap(i, j);
        i++;
    } while (i);
    i = j = 0;
}

Byte prga() {
    Byte s_index;
    i++;
    j = j + S[i];
    swap(i, j);
    s_index = S[i] + S[j];
    return S[s_index];
}

Byte get_key(const int input) {
    key_length = read(input, Key, 256);
    return (key_length != 0);
}

void rc4() {

    Byte buffer[BUFFER_SIZE], keep_ciphering;
    unsigned int index;
    ssize_t read_bytes, written_bytes;
    ksa();

    do {
        read_bytes = read(STDIN, buffer, BUFFER_SIZE);

        fprintf(stderr, "Original Text: ");
        for (index = 0; index < read_bytes; index++) {
            fprintf(stderr, "%02hhX  ", buffer[index]);
        }
        fprintf(stderr, "\n");
        
        fprintf(stderr, "Encrypted Text: ");
        for (index = 0; index < read_bytes; index++) {
            buffer[index] = buffer[index] ^ prga();
            fprintf(stderr, "%02hhX  ",buffer[index]);
        }
        fprintf(stderr, "\n");
        written_bytes = write(STDOUT, buffer, read_bytes);
        keep_ciphering = (read_bytes == BUFFER_SIZE) && (read_bytes == written_bytes);
    } while(keep_ciphering);

}

int main(int argc, char *argv[]) {

    int key_file;
    Byte key;
    if (argc != 2) {
        printf("Usage:\n");
        printf("./rcfour <key file>\n");
        exit(1);
    }

    key_file = open(argv[1], O_RDONLY);
    if (key_file < 3) {
        printf("Can't open the key file\n");
        exit(2);
    }

    key = get_key(key_file);
    if (! key) {
        printf("Can't open the key file\n");
        exit(3);
    }

    rc4();

    close(key_file);
    exit(0);
}