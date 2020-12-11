#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>

static void
parse_input(std::vector<std::vector<int>> &map)
{
    std::fstream     my_input{"input.txt"};
    std::string      line;
    std::vector<int> row;
    int              val;
    while (getline(my_input, line))
    {
        row = std::vector<int>();
        for (auto c : line)
        {
            switch (c)
            {
            case '.':
                val = -1;
                break;
            case 'L':
                val = 0;
                break;
            default:
                val = 1;
                break;
            }
            row.push_back(val);
        }
        map.push_back(row);
    }
}

static void
print_map(std::vector<std::vector<int>> &map)
{
    int i;
    int j;
    for (i = 0; i < map.size(); i++)
    {
        for (j = 0; j < map[i].size(); j++)
        {
            std::cout << std::setw(2) << map[i][j] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << "--------------------------------------" << std::endl;
}

static int
part1_neighbors(std::vector<std::vector<int>> &map, int i, int j)
{
    int r;
    int c;
    int count{};
    int height = map.size();
    int width  = map[0].size();
    for (r = std::max(0, i - 1); r <= std::min(height - 1, i + 1); r++)
    {
        for (c = std::max(0, j - 1); c <= std::min(width - 1, j + 1); c++)
        {
            if (-1 == map[r][c])
            {
                continue; // skip floor spots
            }
            count += map[r][c] & 1;
        }
    }
    count -= map[i][j] & 1; // don't count ourself
    return count;
}

static int
part2_neighbors(std::vector<std::vector<int>> &map, int i, int j)
{
    int                              scale;
    int                              r;
    int                              c;
    int                              count{};
    int                              height = map.size();
    int                              width  = map[0].size();
    std::vector<std::pair<int, int>> neighbors{
        {-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

    for (auto n : neighbors)
    {
        scale = 1;
        while (1)
        {
            r = n.first * scale + i;
            c = n.second * scale + j;
            if (r < 0 || r > height - 1 || c < 0 || c > width - 1)
            {
                break;
            }
            if (map[r][c] != -1)
            {
                count += map[r][c] & 1;
                break;
            }
            scale++;
        }
    }
    return count;
}

static bool
game_of_life(std::vector<std::vector<int>> &map, bool part1)
{
    int  height;
    int  width;
    int  i;
    int  j;
    int  count;
    bool changed{false};

    height = map.size();
    width  = map[0].size();

    for (i = 0; i < height; i++)
    {
        for (j = 0; j < width; j++)
        {
            if (-1 == map[i][j])
            {
                continue; // skip floor spots
            }
            if (part1)
            {
                count = part1_neighbors(map, i, j);
            }
            else
            {
                count = part2_neighbors(map, i, j);
            }
            if (0 == count)
            {
                map[i][j] |= 0b10; // no neighbors
            }
            else if (part1 && count < 4)
            {
                map[i][j] |= (map[i][j] << 1); // keep current status
            }
            else if (!part1 && count < 5)
            {
                map[i][j] |= (map[i][j] << 1); // keep current status
            }
            // else goes/stays empty
        }
    }
    // Reset the map to 0 and 1 and check if it changed
    for (i = 0; i < height; i++)
    {
        for (j = 0; j < width; j++)
        {
            if (-1 == map[i][j])
            {
                continue;
            }
            if ((map[i][j] & 1) << 1 != (map[i][j] & 0b10))
            {
                changed = true;
            }
            map[i][j] >>= 1;
        }
    }
    return changed;
}

static int
solve(bool part1)
{
    std::vector<std::vector<int>> map;
    int                           i;
    int                           j;
    int                           alive{};

    parse_input(map);
    while (game_of_life(map, part1))
    {
        ;
    }
    for (i = 0; i < map.size(); i++)
    {
        for (j = 0; j < map[i].size(); j++)
        {
            if (1 == map[i][j])
            {
                alive++;
            }
        }
    }
    return alive;
}

int
main(int argc, char **argv)
{
    std::cout << solve(true) << "\n";
    std::cout << solve(false) << std::endl;
}