/**
 * @file day2.cpp
 * @author Kyle Fauerbach
 * @brief Solution Advent of Code 2020 Day 2.
 * 
 */

#include <cstring>
#include <fstream>
#include <iostream>
#include <vector>

/**
 * @brief Helper function to split a string on a specified delimiter.
 * 
 * @param str The string to split.
 * @param sep The delimiter
 * @return std::vector<std::string> Vector of the parts of the split string.
 */
static std::vector<std::string>
split(std::string str, std::string sep)
{
    // Cast to cstyle char* so we can use strtok
    char *                   cstr = const_cast<char *>(str.c_str());
    char *                   current;
    std::vector<std::string> arr;

    current = strtok(cstr, sep.c_str());
    while (NULL != current)
    {
        arr.push_back(current);
        current = strtok(NULL, sep.c_str());
    }
    return arr;
}

static int
part1(void)
{
    std::fstream             my_input{"input.txt"};
    std::vector<std::string> words;
    std::vector<std::string> limits;
    std::string              line;
    int                      valid{};
    int                      lo;
    int                      hi;
    int                      char_count;
    char                     check;

    while (getline(my_input, line))
    {
        words  = split(line, " ");
        check  = words[1][0];
        limits = split(words[0], "-");
        lo     = std::stoi(limits[0]);
        hi     = std::stoi(limits[1]);

        char_count = 0;
        for (char my_char : words.back())
        {
            if (my_char == check)
            {
                char_count++;
            }
        }
        if (char_count <= hi && char_count >= lo)
        {
            valid++;
        }
    }

    return valid;
}

static int
part2(void)
{
    std::fstream             my_input{"input.txt"};
    std::vector<std::string> words;
    std::vector<std::string> positions;
    std::string              line;
    int                      valid{};
    int                      pos1;
    int                      pos2;
    char                     check;

    while (getline(my_input, line))
    {
        words     = split(line, " ");
        check     = words[1][0];
        positions = split(words[0], "-");
        // Subtract 1 because provided index starts at 1 not 0.
        pos1 = std::stoi(positions[0]) - 1;
        pos2 = std::stoi(positions[1]) - 1;

        if ((words.back()[pos1] == check) ^ (words.back()[pos2] == check))
        {
            valid++;
        }
    }
    return valid;
}

int
main(int argc, char **argv)
{
    std::cout << part1() << "\n";
    std::cout << part2() << std::endl;
}