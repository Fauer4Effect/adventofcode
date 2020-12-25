#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

static int
part1()
{
    std::fstream     my_input{"input.txt"};
    std::string      line;
    std::vector<int> adapters;
    int              one_v{};
    int              three_v{1};
    int              cur_voltage{};

    while (getline(my_input, line))
    {
        adapters.push_back(std::stoi(line));
    }
    std::sort(adapters.begin(), adapters.end());

    for (auto a : adapters)
    {
        if (1 == (a - cur_voltage))
        {
            one_v++;
        }
        else if (3 == (a - cur_voltage))
        {
            three_v++;
        }

        cur_voltage = a;
    }
    return one_v * three_v;
}

static long
dfs(std::vector<long> &adapters, std::vector<long> &paths, int u)
{
    long   sum{};
    size_t i;
    if (adapters[u] == adapters.back())
    {
        return 1;
    }
    if (!paths[u])
    {
        for (i = 1; i < 4; i++)
        {
            if (u + i > adapters.size() - 1)
            {
                continue;
            }
            if ((adapters[u + i] - adapters[u]) <= 3)
            {
                sum += dfs(adapters, paths, u + i);
            }
        }
        paths[u] = sum;
    }
    return paths[u];
}

static long
part2()
{
    std::fstream      my_input{"input.txt"};
    std::string       line;
    std::vector<long> adapters;

    adapters.push_back(0);
    while (getline(my_input, line))
    {
        adapters.push_back(std::stol(line));
    }
    std::sort(adapters.begin(), adapters.end());
    std::vector<long> paths = std::vector<long>(adapters.size(), 0);
    return dfs(adapters, paths, 0);
}

int
main(int argc, char **argv)
{
    std::cout << part1() << "\n";
    std::cout << part2() << std::endl;
}