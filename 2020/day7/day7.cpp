#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <vector>

#include "../split.h"

// typedef so we don't have to type so much
typedef std::map<std::string, std::vector<std::pair<std::string, int>>>
    bag_map_t;

/**
 * @param part1 If true then we will create a map inner -> outer bags
 * If this is false then we will map outer -> inner
 */
static bag_map_t
parse_input(bool part1)
{
    bag_map_t                bags;
    std::fstream             my_input{"input.txt"};
    std::string              line;
    std::string              outer_color;
    std::string              inner_color;
    size_t                   i;
    std::vector<std::string> splits;

    while (getline(my_input, line))
    {
        if (line.find("no other bags.") != std::string::npos)
        {
            continue;
        }

        splits      = split(line, " ");
        outer_color = splits[0] + " " + splits[1];
        for (i = 4; i < splits.size(); i += 4)
        {
            inner_color = splits[i + 1] + " " + splits[i + 2];
            if (part1)
            {
                bags[inner_color].push_back(std::make_pair(outer_color, 1));
            }
            else
            {
                bags[outer_color].push_back(
                    std::make_pair(inner_color, std::stoi(splits[i])));
            }
        }
    }
    return bags;
}

static int
part1(std::string my_bag)
{
    bag_map_t                bags;
    std::vector<std::string> to_explore{};
    std::string              cur;
    std::set<std::string>    explored{};
    int                      total{};

    bags = parse_input(true);
    to_explore.push_back(my_bag);
    while (!to_explore.empty())
    {
        cur = to_explore.back();
        to_explore.pop_back();
        for (auto i : bags[cur])
        {
            if (explored.count(i.first))
            {
                continue;
            }
            to_explore.push_back(i.first);
            explored.insert(i.first);
            total++;
        }
    }
    return total;
}

static long
get_bags(bag_map_t &bags, std::string bag)
{
    long total{1};
    for (auto i : bags[bag])
    {
        total += i.second * get_bags(bags, i.first);
    }
    return total;
}

static int
part2(std::string my_bag)
{
    bag_map_t                                bags;
    std::vector<std::pair<std::string, int>> to_explore{};
    std::string                              cur;
    int                                      total{};

    bags  = parse_input(false);
    total = get_bags(bags, my_bag);
    return total - 1;
}

int
main(int argc, char **argv)
{
    std::string my_bag{"shiny gold"};
    std::cout << part1(my_bag) << "\n";
    std::cout << part2(my_bag) << std::endl;
}