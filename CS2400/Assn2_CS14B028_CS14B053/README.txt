1) First run make( even if it is not run the shell script will take care).

2) Run server_script.sh(an executable -- if it is not executable do chmod a+x server_script.sh to make it executable). This will set up the server on the required port. The command line arguments are IP, port number and CRC polynomial. The CRC polynomial should be the same polynomial as the one used to channel encode at the server side.

3) Open a new tab in terminal and run client_script.sh. This will print the entropy, average code length and generate the compressed file first. Then it will start transmitting using the CRC polynomial given as command line argument and the error probability of the channel given will be used to generate the errors in the bits.

4) Finally the received file will be decoded.(Though this occurs in the tab of the client side, it is the same file as the one received by the server). Then it decodes the received fiel using the code book generated.

5) Report is attached.
