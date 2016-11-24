# *****************************************************************************************
# Project:              FFT Spectrum Computation
# Subtree:              /home1/hema/FFT/src
# Filename:             Makefile for FFT Program
# Programmer:           Hema A Murthy
# Host System:          Linux
# Date Created:         08/March/2008
# Project:              To compute FFT
# *****************************************************************************************

SRCDIR = ./src
OBJDIR = ./obj
BINDIR = ./bin
INCDIR = ./include
CFLAGS = -g -c -Wall -O -I$(INCDIR)
CC = gcc

all :   $(BINDIR)/ComputeFFT

$(BINDIR)/ComputeFFT : $(OBJDIR)/ComputeFFT.o \
	$(OBJDIR)/FFT.o \
	$(OBJDIR)/AllocateMemory.o 
	$(CC) -g -o $(BINDIR)/ComputeFFT $(OBJDIR)/ComputeFFT.o \
	$(OBJDIR)/FFT.o \
	$(OBJDIR)/AllocateMemory.o -I$(INCDIR) \
	-lm

$(OBJDIR)/ComputeFFT.o : $(SRCDIR)/ComputeFFT.c
	$(CC) $(CFLAGS) -o $(OBJDIR)/ComputeFFT.o $(SRCDIR)/ComputeFFT.c 

$(OBJDIR)/FFT.o : $(SRCDIR)/FFT.c 
	$(CC) $(CFLAGS) -o $(OBJDIR)/FFT.o $(SRCDIR)/FFT.c 

$(OBJDIR)/AllocateMemory.o : $(SRCDIR)/AllocateMemory.c 
	$(CC) $(CFLAGS) -o $(OBJDIR)/AllocateMemory.o $(SRCDIR)/AllocateMemory.c 
clean: 
	rm -fr $(BINDIR)/ComputeFFT $(OBJDIR)/ComputeFFT.o \
	$(OBJDIR)/FFT.o $(OBJDIR)/AllocateMemory.o  



