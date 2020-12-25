#include "../circ_buf.h"
#include <fstream>
#include <iostream>
#include <vector>

static bool
two_sum(circular_buffer<long> &buf, long goal)
{
    for (auto item : buf)
    {
        if (buf.contains(goal - item))
        {
            return true;
        }
    }
    return false;
}

static int
part1()
{
    std::fstream          my_input{"input.txt"};
    std::string           line;
    circular_buffer<long> buf{25};
    size_t                i;
    long                  cur;

    for (i = 0; i < 25; i++)
    {
        getline(my_input, line);
        buf.put(std::stol(line));
    }

    while (getline(my_input, line))
    {
        cur = std::stol(line);
        if (!two_sum(buf, cur))
        {
            return cur;
        }
        buf.put(cur);
    }
    return 0;
}

static int
part2(long invalid)
{
    std::fstream      my_input{"input.txt"};
    std::string       line;
    std::vector<long> nums;
    size_t            lo{};
    size_t            hi;
    int               sum;
    int               smallest;
    int               biggest;
    size_t            i;

    while (getline(my_input, line))
    {
        nums.push_back(std::stol(line));
    }

    while (lo < nums.size())
    {
        hi  = lo;
        sum = nums[lo];
        while (sum < invalid && hi < nums.size())
        {
            sum += nums[++hi];
        }
        if (invalid == sum)
        {
            break;
        }
        lo++;
    }

    sum      = 0;
    smallest = biggest = nums[lo];
    for (i = lo; i <= hi; i++)
    {
        smallest = (smallest < nums[i]) ? smallest : nums[i];
        biggest  = (biggest > nums[i]) ? biggest : nums[i];
        sum += nums[i];
    }

    return smallest + biggest;
}

int
main(int argc, char **argv)
{
    long invalid = part1();
    std::cout << invalid << "\n";
    std::cout << part2(invalid) << std::endl;
}