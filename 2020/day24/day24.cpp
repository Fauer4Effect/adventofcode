#include <fstream>
#include <iostream>
#include <tuple>
#include <vector>
#include "../robin_hood.h"

// https://www.redblobgames.com/grids/hexagons/

using m_key_t = std::tuple<int, int, int>;
using val_t = int;

// custom hash function to use tuple as key in unordered_map
struct key_hash : public std::unary_function<m_key_t, std::size_t>
{
    std::size_t operator()(const m_key_t &k) const
    {
        int hash = 17;
        hash     = 31 * hash + std::get<0>(k);
        hash     = 31 * hash + std::get<1>(k);
        hash     = 31 * hash + std::get<2>(k);
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

using set_t = robin_hood::unordered_flat_set<m_key_t, key_hash, m_key_equal>;
using map_t = robin_hood::unordered_flat_map<m_key_t, val_t, key_hash, m_key_equal>;

static m_key_t get_tile(std::string line)
{
    int x{};
    int y{};
    int z{};
    for (auto i = 0; i < line.size(); i++)
    {
       if ('e' == line[i])
       {
           x++;
           y--;
       }
       else if ('w' == line[i])
       {
           x--;
           y++;
       }
       else if ('n' == line[i])
       {
           z--;
           if ('e' == line[++i])
           {
               x++;
           }
           else
           {
               y++;
           }
       }
       else if ('s' == line[i])
       {
           z++;
           if ('e' == line[++i])
           {
               y--;
           }
           else
           {
               x--;
           }
       }
    }
    return std::make_tuple(x, y, z);
}

static uint64_t part1()
{
    std::fstream my_input{"input.txt"};
    std::string line;
    set_t black_tiles{};
    m_key_t cur_tile;

    while (getline(my_input, line))
    {
        cur_tile = get_tile(line);
        if (black_tiles.find(cur_tile) == black_tiles.end())
        {
            black_tiles.insert(cur_tile);
        }
        else
        {
            black_tiles.erase(cur_tile);
        }
    }

    return black_tiles.size();
}

static val_t get_or_default(map_t &m, const m_key_t &key, val_t default_value)
{
    auto it = m.find(key);
    if (it == m.end())
    {
        return default_value;
    }
    return it->second;
}

static void
update_state(const std::vector<m_key_t> &coords, set_t &tiles)
{
    set_t new_set{};
    map_t neighbors{};
    m_key_t new_tile;
    
    // Get the neighbors of the black nodes and say that those
    // nodes have a black one as a neighbor
    for (auto [x1, y1, z1] : tiles)
    {
        for (auto [x2, y2, z2] : coords)
        {
            new_tile = std::make_tuple(x1+x2, y1+y2,z1+z2); 

            neighbors[new_tile] = get_or_default(neighbors, new_tile, 0) + 1;
        }
    }

    // now we have to go through and find which ones
    // need to get set
    for (auto t : tiles)
    {
        // if tile is black and neighbors <= 2
        // it stays black
        if (neighbors.find(t) != neighbors.end() && neighbors[t] <= 2)
        {
            new_set.insert(t);
        }
    }
    for (auto [k, v] : neighbors)
    {
        if (v != 2)
        {
            continue;
        }
        // if it's a white tile and has exactly 2 black neighbors
        // it becomes black
        if (tiles.find(k) == tiles.end())
        {
            new_set.insert(k);
        }
    }
    tiles = new_set;
}

static uint64_t part2()
{
    std::fstream my_input{"input.txt"};
    std::string line;
    set_t black_tiles{};
    std::vector<m_key_t> keys;
    std::vector<m_key_t> neighbors{{1,-1,0}, {1,0,-1},{0,1,-1},{-1,1,0},{-1,0,1},{0,-1,1}};
    m_key_t cur_tile;

    // initialize set
    while (getline(my_input, line))
    {
        cur_tile = get_tile(line);
        if (black_tiles.find(cur_tile) == black_tiles.end())
        {
            black_tiles.insert(cur_tile);
        }
        else
        {
            black_tiles.erase(cur_tile);
        }
    }

    for (auto day = 0; day < 100; day++)
    {
        update_state(neighbors, black_tiles);
    }

    return black_tiles.size();
}

int main(int argc, char **argv)
{
    std::cout << part1() << "\n";
    std::cout << part2() << std::endl;
}
