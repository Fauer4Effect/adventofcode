/**
 * @file day1.cpp
 * @author Kyle Fauerbach
 * @brief Solution to Advent of Code 2020 Day 1.
 *
 */
#include <fstream>
#include <iostream>
#include <unordered_set>

/**
 * @brief Use hashset to calculate 2sum.
 *
 * @param goal What we want the number to sum to.
 * @return std::pair<int, int> Pair of the two numbers.
 */
static std::pair<int, int>
two_sum(int goal)
{
    std::fstream            my_input{"input.txt"};
    std::string             line;
    std::unordered_set<int> complements;
    std::pair<int, int>     retval;
    int                     complement;
    int                     line_int;

    while (getline(my_input, line))
    {
        line_int   = std::stoi(line);
        complement = goal - line_int;
        auto found = complements.find(complement);
        if (complements.end() != found)
        {
            retval = std::make_pair(complement, line_int);
            break;
        }
        else
        {
            complements.insert(line_int);
        }
    }

    my_input.close();
    return retval;
}

/**
 * @brief Solve 3sum utilizing above 2sum solution.
 *
 * @param goal What we want to sum to.
 * @return std::tuple<int, int, int> Tuple of the three numbers.
 */
static std::tuple<int, int, int>
three_sum(int goal)
{
    std::fstream              my_input{"input.txt"};
    std::string               line;
    std::tuple<int, int, int> retval;
    int                       line_int;

    while (getline(my_input, line))
    {
        line_int          = std::stoi(line);
        const auto [a, b] = two_sum(goal - line_int);
        if (0 != a && 0 != b)
        {
            retval = std::make_tuple(line_int, a, b);
        }
    }
    return retval;
}

int
main(int argc, char **argv)
{
    int                 goal = 2020;
    std::pair<int, int> ans  = two_sum(goal);
    std::cout << ans.first * ans.second << "\n";
    const auto [a, b, c] = three_sum(goal);
    std::cout << a * b * c << std::endl;
}
