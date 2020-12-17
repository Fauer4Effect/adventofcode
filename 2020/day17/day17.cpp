#include "../split.h"
#include <algorithm>
#include <fstream>
#include <iostream>
#include <tuple>
#include <unordered_map>

// typedef so we don't have to type as much
// typedef std::tuple<int, int, int> m_key_t;
typedef std::tuple<int, int, int, int> m_key_t;
typedef int                            val_t;

// custom hash function to use tuple as key in unordered_map
struct key_hash : public std::unary_function<m_key_t, std::size_t>
{
    std::size_t operator()(const m_key_t &k) const
    {
        // return std::get<0>(k) ^ std::get<1>(k) ^ std::get<2>(k);
        return std::get<0>(k) ^ std::get<1>(k) ^ std::get<2>(k) ^
               std::get<3>(k);
    }
};

// custom equality to use tuple as key in unordered map
struct m_key_equal : public std::binary_function<m_key_t, m_key_t, bool>
{
    bool operator()(const m_key_t &v0, const m_key_t &v1) const
    {
        return (
            // std::get<0>(v0) == std::get<0>(v1) &&
            // std::get<1>(v0) == std::get<1>(v1) &&
            // std::get<2>(v0) == std::get<2>(v1)

            /*std::get<0>(v0) == std::get<0>(v1) &&
            std::get<1>(v0) == std::get<1>(v1) &&
            std::get<2>(v0) == std::get<2>(v1) &&
            std::get<3>(v0) == std::get<3>(v1));*/
            v0 == v1
        );
    }
};

// typedef for our custom map
typedef std::unordered_map<m_key_t, val_t, key_hash, m_key_equal> map_t;

// Helper function to get a default value from unordered map if it's not present
val_t
get_or_default(map_t &m, const m_key_t &key, val_t default_value)
{
    auto it = m.find(key);
    if (it == m.end())
    {
        // m[key] = default_value;
        // return m[key];
        return default_value;
    }
    return it->second;
}

static void
update_state(std::vector<m_key_t> &neighbors, map_t &field, const m_key_t &cur)
{
    std::tuple<int, int, int> neighbor;
    int                       current;
    int                       living_neighbors{};
    // auto [x1, y1, z1] = cur;
    auto [x1, y1, z1, w1] = cur;

    // for (auto [x2, y2, z2] : neighbors)
    for (auto [x2, y2, z2, w2] : neighbors)
    {
        // if (std::abs(get_or_default(field,
        // std::make_tuple(x1+x2,y1+y2,z1+z2), 0)) == 1)
        if (std::abs(get_or_default(
                field, std::make_tuple(x1 + x2, y1 + y2, z1 + z2, w1 + w2),
                0)) == 1)
        {
            living_neighbors++;
        }
    }

    current = get_or_default(field, cur, 0);
    if (1 == current && (living_neighbors < 2 || living_neighbors > 3))
    {
        field[cur] = -1;
    }
    else if (0 == current && 3 == living_neighbors)
    {
        field[cur] = 2;
    }
}

/*
static long part1()
{
    std::fstream my_input{"input.txt"};
    std::string line;
    std::vector<std::string> splits;
    std::vector<std::tuple<int, int, int>> neighbors {};
    std::vector<m_key_t> keys;
    map_t field{};
    int x{};
    int y;
    int start_size;
    long alive{};

    while (getline(my_input, line))
    {
        start_size = line.size();
        for (y = 0; y < line.size(); y++)
        {
            field[std::make_tuple(x, y, 0)] = ('#' == line[y]);
        }
        x++;
    }

    for (auto x = -1; x < 2; x++)
    {
        for (auto y = -1; y < 2; y++)
        {
            for (auto z = -1; z < 2; z++)
            {
                if (x == 0 && y == 0 && z == 0)
                {
                    continue;
                }
                neighbors.push_back(std::make_tuple(x, y, z));
            }
        }
    }

    for (auto round = 0; round < 6; round++)
    {
        // Get list of keys first so we don't modify while we loop
        keys.clear();
        for (auto x = -1-round; x < 1+start_size+round; x++)
        {
            for (auto y = -1-round; y < 1+start_size+round; y++)
            {
                for (auto z = -1-round; z < 2+round; z++)
                {
                    keys.push_back(std::make_tuple(x, y, z));
                }
            }
        }

        // do the updates
        for (auto key : keys)
        {
            update_state(neighbors, field, key);
        }

        // reset the field to 0 and 1
        for (auto [key, val] : field)
        {
            field[key] = (val > 0);
        }
    }

    for (auto [key, val] : field)
    {
        alive += val;
    }

    return alive;
}
*/

static long
part2()
{
    std::fstream             my_input{"input.txt"};
    std::string              line;
    std::vector<std::string> splits;
    std::vector<m_key_t>     neighbors{};
    std::vector<m_key_t>     keys;
    map_t                    field{};
    int                      x{};
    int                      y;
    int                      start_size;
    long                     alive{};

    while (getline(my_input, line))
    {
        start_size = line.size();
        for (y = 0; y < line.size(); y++)
        {
            field[std::make_tuple(x, y, 0, 0)] = ('#' == line[y]);
        }
        x++;
    }

    for (auto x = -1; x < 2; x++)
    {
        for (auto y = -1; y < 2; y++)
        {
            for (auto z = -1; z < 2; z++)
            {
                for (auto w = -1; w < 2; w++)
                {
                    if (x == 0 && y == 0 && z == 0 && w == 0)
                    {
                        continue;
                    }
                    neighbors.push_back(std::make_tuple(x, y, z, w));
                }
            }
        }
    }

    int min_x = 0;
    int min_y = 0;
    int min_z = 0;
    int min_w = 0;
    int max_x = start_size;
    int max_y = start_size;
    int max_z = 1;
    int max_w = 1;

    for (auto round = 0; round < 6; round++)
    {
        min_x--;
        max_x++;
        min_y--;
        max_y++;
        min_w--;
        max_w++;
        min_z--;
        max_z++;

        // Get list of keys first so we don't modify while we loop
        keys.clear();
        for (auto x = min_x; x < max_x; x++)
        {
            for (auto y = min_y; y < max_y; y++)
            {
                for (auto z = min_z; z < max_z; z++)
                {
                    for (auto w = min_w; w < max_w; w++)
                    {
                        keys.push_back(std::make_tuple(x, y, z, w));
                    }
                }
            }
        }

        // do the updates
        for (auto key : keys)
        {
            update_state(neighbors, field, key);
        }

        // reset the field to 0 and 1
        for (auto [key, val] : field)
        {
            field[key] = (val > 0);
        }

        for (auto [key, val] : field)
        {
            if (val)
            {
                auto [x, y, z, w] = key;
                min_x             = (min_x < x) ? min_x : x;
                max_x             = (max_x > x) ? max_x : x;
                min_y             = (min_y < y) ? min_y : y;
                max_y             = (max_y > y) ? max_y : y;
                min_z             = (min_z < z) ? min_z : z;
                max_z             = (max_z > z) ? max_z : z;
                min_w             = (min_w < w) ? min_w : w;
                max_w             = (max_w > w) ? max_w : w;
            }
        }
    }

    for (auto [key, val] : field)
    {
        alive += val;
    }

    return alive;
}

int
main(int argc, char **argv)
{
    // std::cout << part1() << "\n";
    std::cout << part2() << std::endl;
}
