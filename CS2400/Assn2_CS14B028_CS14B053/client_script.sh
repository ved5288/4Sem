#!/bin/sh
#Shell script to compile the files and run the client
gcc -o huffman huffman_code.c -lm
./huffman text_file.txt #Change the file name here.
gcc -o code_gen huffman_code_generator.c -lm
./code_gen
gcc -o compress compress_file.c -lm
./compress text_file.txt #Change the file name here.
./bin/Client 127.0.0.1 1400 127.0.0.1 1200 101100 0.15 #Change the CRC polynomial and error probability here. Also change the CRC polynomial in server_script.sh
gcc -o decode decode_file.c -lm
./decode received_data.txt decoded_file1.txt 
diff -a decoded_file1.txt text_file.txt		#Change the file name here.
