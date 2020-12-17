#include "../split.h"
#include "robin_hood.h"
#include <fstream>
#include <iostream>
#include <tuple>

#define PART1 0

#if PART1 == 1
typedef std::tuple<int, int, int> m_key_t;
#else
typedef std::tuple<int, int, int, int> m_key_t;
#endif // typedef key type

typedef int val_t;

// custom hash function to use tuple as key in unordered_map
struct key_hash : public std::unary_function<m_key_t, std::size_t>
{
    std::size_t operator()(const m_key_t &k) const
    {
        int hash = 17;
        hash     = 31 * hash + std::get<0>(k);
        hash     = 31 * hash + std::get<1>(k);
        hash     = 31 * hash + std::get<2>(k);
#if PART1 == 0
        hash = 31 * hash + std::get<3>(k);
#endif // hash time if we have it
        return hash;
    }
};

// custom equality to use tuple as key in unordered map
struct m_key_equal : public std::binary_function<m_key_t, m_key_t, bool>
{
    bool operator()(const m_key_t &v0, const m_key_t &v1) const
    {
        return v0 == v1;
    }
};

// typedef for our custom map
typedef robin_hood::unordered_flat_map<m_key_t, val_t, key_hash, m_key_equal>
    map_t;

// Helper function to get a default value from unordered map if it's not present
val_t
get_or_default(map_t &m, const m_key_t &key, val_t default_value)
{
    auto it = m.find(key);
    if (it == m.end())
    {
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
#if PART1 == 1
    auto [x1, y1, z1] = cur;
#else
    auto [x1, y1, z1, w1] = cur;
#endif // decompose tuple

#if PART1 == 1
    for (auto [x2, y2, z2] : neighbors)
#else
    for (auto [x2, y2, z2, w2] : neighbors)
#endif // loop based on part1 or 2
    {

#if PART1 == 1
        if (std::abs(get_or_default(
                field, std::make_tuple(x1 + x2, y1 + y2, z1 + z2), 0)) == 1)
#else
        if (std::abs(get_or_default(
                field, std::make_tuple(x1 + x2, y1 + y2, z1 + z2, w1 + w2),
                0)) == 1)
#endif // if based on size of tuple
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

static long
solve()
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
    int                      min_x;
    int                      max_x;
    int                      min_y;
    int                      max_y;
    int                      min_z;
    int                      max_z;
#if PART1 == 0
    int                      min_w;
    int                      max_w;
#endif

    while (getline(my_input, line))
    {
        start_size = line.size();
        for (y = 0; y < line.size(); y++)
        {
#if PART1 == 1
            field[std::make_tuple(x, y, 0)] = ('#' == line[y]);
#else
            field[std::make_tuple(x, y, 0, 0)] = ('#' == line[y]);
#endif
        }
        x++;
    }

#if PART1 == 1
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
#else
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
#endif // Neighbors based on dimensions

    min_x = 0;
    max_x = start_size;
    min_y = 0;
    max_y = start_size;
    min_z = 0;
    max_z = 1;
#if PART1 == 0
    min_w = 0;
    max_w = 1;
#endif // Do we need time

    for (auto round = 0; round < 6; round++)
    {
        min_x--;
        max_x++;
        min_y--;
        max_y++;
        min_z--;
        max_z++;
#if PART1 == 0
        min_w--;
        max_w++;
#endif

        // Get list of keys first so we don't modify while we loop
        keys.clear();
#if PART1 == 1
        for (auto x = min_x; x < max_x; x++)
        {
            for (auto y = min_y; y < max_y; y++)
            {
                for (auto z = min_z; z < max_z; z++)
                {
                    keys.push_back(std::make_tuple(x, y, z));
                }
            }
        }
#else
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
#endif // 4-tuple keys if part2

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
#if PART1 == 1
                auto [x, y, z] = key;
#else
                auto [x, y, z, w] = key;
#endif
                min_x = std::min(min_x, x);
                max_x = std::max(max_x, x);
                min_y = std::min(min_y, y);
                max_y = std::max(max_y, y);
                min_z = std::min(min_z, z);
                max_z = std::max(max_z, z);
#if PART1 == 0
                min_w = std::min(min_w, w);
                max_w = std::max(max_w, w);
#endif
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
    std::cout << solve() << std::endl;
}
