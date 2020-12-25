#include <fstream>
#include <iostream>
#include <vector>

static std::vector<std::string>
fill_map(void)
{
    std::fstream             my_input{"input.txt"};
    std::string              line{};
    std::vector<std::string> map{};

    while (getline(my_input, line))
    {
        map.push_back(line);
    }

    return map;
}

static int
part1(std::vector<std::string> map, int right, int down)
{
    int  trees{};
    int  x_pos{};
    int  y_pos{};
    int  num_rows;
    int  width;
    char tree{'#'};

    num_rows = map.size();
    width    = map.back().length();

    for (; y_pos < num_rows; y_pos += down, x_pos = (x_pos + right) % width)
    {
        if (tree == map[y_pos][x_pos])
        {
            trees++;
        }
    }

    return trees;
}

static long
part2(std::vector<std::string> map)
{
    long                             trees{1};
    std::vector<std::pair<int, int>> slopes{
        {1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}};

    for (auto slope : slopes)
    {
        trees *= part1(map, slope.first, slope.second);
    }

    return trees;
}

int
main(int argc, char **argv)
{
    std::vector<std::string> map = fill_map();
    std::cout << part1(map, 3, 1) << "\n";
    std::cout << part2(map) << "\n";
}