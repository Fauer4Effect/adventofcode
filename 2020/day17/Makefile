CC = g++
CFLAGS = -g -Wall -Ofast -std=c++17 
TARGET = day17

all: $(TARGET)

$(TARGET): $(TARGET).cpp
	$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).cpp ../split.cpp

clean:
	$(RM) $(TARGET) 
