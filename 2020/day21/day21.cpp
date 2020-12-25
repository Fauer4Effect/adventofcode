#include "../join.h"
#include "../split.h"
#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <unordered_set>
#include <vector>

static void
solve()
{

    // keep a map of allergen to set of ingredients
    // when we have a new food, check the allergens in that food
    // if there is an ingredient in the new food that isn't in
    // the allergen set then that ingredient is not an allergen
    // and anything in the allergen set that isn't in the new
    // food is also not an allergen
    // if we end up having an allergen where the set is still bigger
    // than one then we have to go through the list and remove
    // the single allergens that matched others

    std::fstream my_input{"input.txt"};
    std::string  line;
    std::map<std::string, std::unordered_set<std::string>> allergens;
    std::vector<std::string>                               splits;
    std::vector<std::string>                               ingredients;
    std::vector<std::string>                               allergy;
    std::vector<std::string>                               all;
    std::vector<std::string>                               dangerous;
    std::unordered_set<std::string>                        tmp;
    std::unordered_set<std::string>                        possible;
    std::unordered_set<std::string>                        confirmed;
    std::string                                            danger_str;
    bool                                                   done{false};
    std::uint64_t                                          ans{};

    while (getline(my_input, line))
    {
        line.erase(std::remove(line.begin(), line.end(), '('), line.end());
        line.erase(std::remove(line.begin(), line.end(), ')'), line.end());
        splits      = split(line, " contains ");
        ingredients = split(splits[0], " ");
        allergy     = split(splits[1], ", ");

        for (auto i : ingredients)
        {
            all.push_back(i);
        }

        for (auto allerg : allergy)
        {
            if (allergens.find(allerg) == allergens.end())
            {
                // haven't seen this one before
                tmp = std::unordered_set<std::string>();
                for (auto i : ingredients)
                {
                    tmp.insert(i);
                }
                allergens[allerg] = tmp;
            }
            else
            {
                // we've already seen this allergen so we need to find which
                // ingredient it is
                possible = allergens[allerg];
                tmp      = std::unordered_set<std::string>();
                for (auto i : ingredients)
                {
                    if (possible.find(i) != possible.end())
                    {
                        tmp.insert(i);
                    }
                }
                allergens[allerg] = tmp;
            }
        }
    }

    while (!done)
    {
        done = true;
        for (auto [allergen, possible] : allergens)
        {
            if (possible.size() == 1)
            {
                confirmed.insert(*possible.begin());
                // remove this allergen from other sets
                for (auto &[a2, p2] : allergens)
                {
                    if (allergen != a2)
                    {
                        p2.erase(*possible.begin());
                    }
                }
            }
            else
            {
                done = false;
            }
        }
    }

    for (auto i : all)
    {
        if (confirmed.find(i) == confirmed.end())
        {
            ans++;
        }
    }

    for (auto [allergen, cause] : allergens)
    {
        dangerous.push_back(*cause.begin());
    }

    danger_str = join(dangerous.begin(), dangerous.end(), ",");

    std::cout << "Part 1: " << ans << std::endl;
    std::cout << "Part 2: " << danger_str << std::endl;
}

int
main(int argc, char **argv)
{
    solve();
}
