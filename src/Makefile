# A really simple make file because this code is not complex!



FLAGS := $(FLAGS) -Wall
override CFLAGS += $(shell pkg-config --cflags --libs python3-embed)

all:
	gcc $(FLAGS) -o fasta_validate ./fasta_validate.c $(CFLAGS) -lz

install: all
	cp fasta_validate /usr/local/bin

test: all
	./test.sh

clean:
	rm -f fasta_validate
