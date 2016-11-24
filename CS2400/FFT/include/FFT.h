#ifndef FFT_H
#define FFT_H
/* complex number type */

typedef struct cmplx { float re,im ; }complex;
void Cfft(complex  *a,complex *b, int m, int n, int nsign);
void Cstore(int n);
#endif
