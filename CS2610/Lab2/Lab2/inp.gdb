set debug remote 0
set remotebaud 38400
target remote /dev/ttyS0


load out.out
load out.out
c

i reg
x/x 0xd200
x/x 0xd208
