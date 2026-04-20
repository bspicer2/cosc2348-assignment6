CC = gcc
CFLAGS = -Wall -g

OBJS = main.o addition.o subtraction.o multiplication.o division.o

calculator: $(OBJS)
	$(CC) $(CFLAGS) -o calculator $(OBJS)

%.o: %.c operations.h
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f *.o calculator
