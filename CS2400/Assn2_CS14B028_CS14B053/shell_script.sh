#!/bin/sh
#Shell script to compile the files and run the server
make
gcc -o huffman huffman_code.c -lm
./huffman text_file.txt #Change the file name here.
gcc -o code_gen huffman_code_generator.c -lm
./code_gen
gcc -o compress compress_file.c -lm
./compress text_file.txt #Change the file name here.
./bin/Client 127.0.0.1 1400 127.0.0.1 1200 101100 0.1 #Change the error probability here.
gcc -o decode decode_file.c -lm
./decode received_data.txt decoded_file1.txt #Change the file name here.
diff -a decoded_file1.txt text_file.txt
