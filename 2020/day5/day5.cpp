#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

static std::vector<int>
get_seat_vals(void)
{
    std::fstream     my_input{"input.txt"};
    std::string      line;
    int              lo;
    int              hi;
    int              left;
    int              right;
    int              value;
    std::vector<int> seats{};

    while (getline(my_input, line))
    {
        lo    = 0;
        hi    = 127;
        left  = 0;
        right = 7;
        for (auto chr : line)
        {
            if (chr == 'F')
            {
                hi = (lo + hi) / 2;
            }
            else if (chr == 'B')
            {
                lo = ((lo + hi) / 2) + 1;
            }
            else if (chr == 'L')
            {
                right = (left + right) / 2;
            }
            else if (chr == 'R')
            {
                left = ((left + right) / 2) + 1;
            }
        }
        value = lo * 8 + left;
        seats.push_back(value);
    }
    return seats;
}

static int
part1(void)
{
    std::vector<int> seats;
    int              highest{};

    seats = get_seat_vals();
    for (auto val : seats)
    {
        highest = std::max(highest, val);
    }
    return highest;
}

static int
part2()
{
    std::vector<int> seats;
    size_t           i;
    int              mine{};

    seats = get_seat_vals();
    std::sort(seats.begin(), seats.end());

    for (i = 0; i < seats.size() - 1; i++)
    {
        if (seats[i + 1] - 1 != seats[i])
        {
            mine = seats[i + 1] - 1;
        }
    }
    return mine;
}

int
main(int argc, char **argv)
{
    std::cout << part1() << "\n";
    std::cout << part2() << std::endl;
}