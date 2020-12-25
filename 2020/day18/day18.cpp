#include "../InfInt.h"
#include <algorithm>
#include <ctype.h>
#include <fstream>
#include <iostream>
#include <vector>

static InfInt
do_op(char op, InfInt l, InfInt r)
{
    if ('+' == op)
    {
        return l + r;
    }
    else
    {
        return l * r;
    }
}

static std::pair<InfInt, int>
calc1(std::string expr, size_t i)
{
    InfInt l{};
    char   op{' '};
    while (i < expr.size())
    {
        if (isdigit(expr[i]))
        {
            if (' ' == op)
            {
                l = expr[i] - '0';
            }
            else
            {
                l  = do_op(op, l, (expr[i] - '0'));
                op = ' ';
            }
        }
        else if ('(' == expr[i])
        {
            if (' ' == op)
            {
                auto [sum, index] = calc1(expr, ++i);
                l                 = sum;
                i                 = index;
            }
            else
            {
                auto [sum, index] = calc1(expr, ++i);
                l                 = do_op(op, l, sum);
                i                 = index;
                op                = ' ';
            }
            continue;
        }
        else if (')' == expr[i])
        {
            return std::make_pair(l, i + 1);
        }
        else
        {
            op = expr[i];
        }
        i++;
    }
    return std::make_pair(l, i + 1);
}

// Addition has priority over multiplication
static std::pair<InfInt, int>
calc2(std::string expr, size_t i)
{
    std::vector<InfInt> nums{};
    InfInt              l{};
    char                op{' '};
    while (i < expr.size())
    {
        if (isdigit(expr[i]))
        {
            if (' ' == op)
            {
                nums.push_back(expr[i] - '0');
            }
            else
            {
                if ('+' == op)
                {
                    nums.back() += (expr[i] - '0');
                }
                else
                {
                    nums.push_back(expr[i] - '0');
                }
                op = ' ';
            }
        }
        else if ('(' == expr[i])
        {
            if (' ' == op)
            {
                auto [sum, index] = calc2(expr, ++i);
                nums.push_back(sum);
                i = index;
            }
            else
            {
                auto [sum, index] = calc2(expr, ++i);
                if ('+' == op)
                {
                    nums.back() += sum;
                }
                else
                {
                    nums.push_back(sum);
                }
                i  = index;
                op = ' ';
            }
            continue;
        }
        else if (')' == expr[i])
        {
            l = 1;
            for (auto n : nums)
            {
                l *= n;
            }
            return std::make_pair(l, i + 1);
        }
        else
        {
            op = expr[i];
        }
        i++;
    }
    l = 1;
    for (auto n : nums)
    {
        l *= n;
    }
    return std::make_pair(l, i + 1);
}

static InfInt
part1()
{
    std::fstream my_input{"input.txt"};
    std::string  line;
    InfInt       ans{};

    while (getline(my_input, line))
    {
        line.erase(std::remove_if(line.begin(), line.end(), isspace),
                   line.end());
        auto [calc, trash] = calc1(line, 0);
        ans += calc;
    }
    return ans;
}

static InfInt
part2()
{
    std::fstream my_input{"input.txt"};
    std::string  line;
    InfInt       ans{};

    while (getline(my_input, line))
    {
        line.erase(std::remove_if(line.begin(), line.end(), isspace),
                   line.end());
        auto [calc, trash] = calc2(line, 0);
        ans += calc;
    }
    return ans;
    return 0;
}

int
main(int argc, char **argv)
{
    std::cout << part1() << "\n";
    std::cout << part2() << std::endl;
}
