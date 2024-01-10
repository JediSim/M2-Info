FLAGS = -std=c99 -Wall -Wextra -pedantic -Werror -O4 
# FLAGS = -std=c99 -Wall -Wextra -pedantic -Werror -Wno-unused-parameter -O4
# FLAGS = -std=c99 -Wall -Wextra -Werror -pedantic -O0 -pg -no-pie
LFLAGS = -lcrypto -lssl -lm

EXE = rbt

GCC = gcc

# utils.c config.c functions.c hash.c stats.c tables.c brute-force.c crack.c test.c 

FILES = main.c
O_FILES = $(FILES:.c=.o)

all: $(EXE)

%.o: %.c rbt.h
	$(GCC) $(FLAGS) -c $<

$(EXE): $(O_FILES)
	$(GCC) $(FLAGS) $(O_FILES) -o $(EXE) $(LFLAGS)

clean:
	rm -f *.o a.out gmon.out

veryclean: clean
	rm -f $(EXE)

.PHONY: all clean veryclean
