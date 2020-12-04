#include "split.h"
#include <cstring>

std::vector<std::string>
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