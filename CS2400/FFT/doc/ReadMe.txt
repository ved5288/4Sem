			FFT Programs
			============

1. First untar the tarball.
2. cd to FFT
3. To compile 
     make -f Makefile 
4. The program takes as input:
    Infile (data in a column -- text)
    fftOrder (FFT Order)
    fftSize (2**fftOrder)
    Outfile (data in a column -- text) -- contains the magnitude spectrum

5. If you wish to use the FFT functions in your programs:
   You need create a complex array with the real part containing
   the data whose FFT is to be computed and the imaginary part
   set to zero.

6. The FFT uses indices from 1 - N, as opposed to 0-(N-1).  You
   need to allocate 1 extra element for this.
