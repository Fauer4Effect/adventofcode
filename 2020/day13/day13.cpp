#include "../split.h"
#include <fstream>
#include <iostream>
#include <limits>
#include <vector>

static long
part1()
{
    std::fstream             my_input{"input.txt"};
    std::string              line;
    std::vector<std::string> split_line;
    std::vector<long>        buses;
    long                     arrival;
    long                     tmp_wait;
    long                     wait_time = std::numeric_limits<long>::max();
    long                     best_bus;

    getline(my_input, line);
    arrival = std::stol(line);
    getline(my_input, line);
    split_line = split(line, ",");

    for (auto b : split_line)
    {
        if (b.compare("x"))
        {
            buses.push_back(std::stol(b));
        }
    }

    for (auto bus : buses)
    {
        tmp_wait = bus - (arrival % bus);
        if (tmp_wait < wait_time)
        {
            wait_time = tmp_wait;
            best_bus  = bus;
        }
    }
    return best_bus * wait_time;
}

static long
inverse_modulus(long a, long m)
{
    long m0 = m;
    long y  = 0;
    long x  = 1;
    long q;
    long tmp;

    if (m == 1)
    {
        return 0;
    }

    while (a > 1)
    {
        q   = a / m;
        tmp = a;
        a   = m;
        m   = tmp % m;
        tmp = x;
        x   = y;
        y   = tmp - q * y;
    }

    if (x < 0)
    {
        x += m0;
    }
    return x;
}

static long
part2()
{
    std::fstream                       my_input{"input.txt"};
    std::string                        line;
    std::vector<std::string>           split_line;
    std::vector<std::pair<long, long>> buses;
    long                               product{1};
    long                               res{0};
    long                               partial;
    long                               bus;

    // we want to find timestamp so for all buses
    // timestamp + delay = k * bos number
    // This is basically the chinese remainder theorem
    // A solution is a timestamp that divided by the first bus number remainder
    // is 0. remainder for the second bus number is 1

    getline(my_input, line); // just throw this away
    getline(my_input, line);
    split_line = split(line, ",");
    for (auto i = 0; i < split_line.size(); i++)
    {
        if (split_line[i].compare("x"))
        {
            bus = std::stol(split_line[i]);
            buses.push_back(std::make_pair(bus, bus - i));
            product *= bus;
        }
    }

    for (auto pair : buses)
    {
        auto [divider, remainder] = pair;
        partial                   = product / divider;
        res += remainder * inverse_modulus(partial, divider) * partial;
    }

    return res % product;
}

int
main(int argc, char **argv)
{
    std::cout << part1() << "\n";
    std::cout << part2() << std::endl;
}