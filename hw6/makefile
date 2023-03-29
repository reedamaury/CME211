main: main.o hw6.o image.o
	g++ -o main main.o hw6.o image.o -ljpeg
%.o: %.cpp hw6.hpp image.hpp
	g++ -c -o $@ $< -O3 -Wall -Wextra -Wconversion -pedantic -std=c++11 
.PHONY: clean
clean: 
	rm -f main.o hw6.o image.o main
