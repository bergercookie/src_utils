# Courtesy of  http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/
# Modified for the projecteuler challenges
# Sun May 3 02:14:13 CEST 2015, nickkouk

CC=gcc
CFLAGS = -I$(IDIR) -Wall -g
SRC=$(wildcard *.c)
LIBS =  -lgsl -lm
IDIR = ./include
LDIR= ./lib
ODIR= ./obj

_DEPS = sup_funs.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

_OBJ = sup_funs.o prob10.o 
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))


$(ODIR)/%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

euler_exe: $(OBJ)
	gcc -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean
clean:
	rm -f $(ODIR)/*.o 

