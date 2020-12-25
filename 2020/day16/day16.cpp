#include "../split.h"
#include <fstream>
#include <iostream>
#include <numeric>
#include <unordered_map>

class Rule
{
  public:
    Rule() {}

    bool is_valid(int value)
    {
        for (auto [lo, hi] : limits)
        {
            if (value >= lo && value <= hi)
            {
                return true;
            }
        }
        return false;
    }

    std::vector<std::pair<int, int>> limits{};
};

static void
parse_input(std::fstream &my_input, std::unordered_map<int, Rule> &rules)
{
    std::string              line;
    std::vector<std::string> splits;
    Rule                     r;
    int                      idx{};
    int                      delim;
    int                      lo;
    int                      hi;

    getline(my_input, line);
    while (!line.empty())
    {
        r      = Rule();
        splits = split(line, " ");

        delim = splits[splits.size() - 1].find("-");
        lo    = std::stoi(splits[splits.size() - 1].substr(0, delim));
        hi    = std::stoi(splits[splits.size() - 1].substr(delim + 1));
        r.limits.push_back(std::make_pair(lo, hi));

        delim = splits[splits.size() - 3].find("-");
        lo    = std::stoi(splits[splits.size() - 3].substr(0, delim));
        hi    = std::stoi(splits[splits.size() - 3].substr(delim + 1));
        r.limits.push_back(std::make_pair(lo, hi));

        rules[idx++] = r;
        getline(my_input, line);
    }
}

static long
part1()
{
    std::fstream                  my_input{"input.txt"};
    std::string                   line;
    std::unordered_map<int, Rule> rules{};
    std::vector<std::string>      ticket;
    long                          invalid{};
    bool                          valid;
    Rule                          rule;

    parse_input(my_input, rules);

    getline(my_input, line);
    getline(my_input, line);
    getline(my_input, line);
    getline(my_input, line);

    while (getline(my_input, line))
    {
        ticket = split(line, ",");
        for (auto field : ticket)
        {
            valid = false;
            for (auto [idx, rule] : rules)
            {
                valid |= rule.is_valid(std::stoi(field));
            }
            if (!valid)
            {
                invalid += std::stoi(field);
            }
        }
    }
    return invalid;
}

static long
part2()
{
    std::fstream                              my_input{"input.txt"};
    std::string                               line;
    std::unordered_map<int, Rule>             rules{};
    std::unordered_map<int, std::vector<int>> possible;
    std::vector<std::string>                  ticket;
    std::vector<std::string>                  my_ticket;
    long                                      ans{1};
    bool                                      valid;
    Rule                                      rule;
    int                                       field_idx;

    parse_input(my_input, rules);

    getline(my_input, line);
    getline(my_input, line);
    my_ticket = split(line, ",");
    getline(my_input, line);
    getline(my_input, line);

    for (auto i = 0; i < rules.size(); i++)
    {
        possible[i] = std::vector<int>(my_ticket.size(), 1);
    }

    while (getline(my_input, line))
    {
        valid  = true;
        ticket = split(line, ",");
        for (auto field : ticket)
        {
            valid = false;
            for (auto [idx, rule] : rules)
            {
                valid |= rule.is_valid(std::stoi(field));
            }
            if (!valid)
            {
                break;
            }
        }
        if (!valid)
        {
            continue;
        }

        // Now we know the ticket is valid
        // For every field, mark the rules that might be true for that field
        for (auto j = 0; j < ticket.size(); j++)
        {
            for (auto [idx, rule] : rules)
            {
                if (!rule.is_valid(std::stoi(ticket[j])))
                {
                    possible[idx][j] = 0;
                }
            }
        }
    }

    // now go through and find a rule with only one field
    // make sure that field is unset for other rules
    bool done;
    while (true)
    {
        done = true;
        for (auto [idx, r] : possible)
        {
            int sum =
                std::accumulate(r.begin(), r.end(), decltype(r)::value_type(0));
            if (sum == 1)
            {
                // this rule has only 1 field
                // find that field
                for (field_idx = 0; field_idx < r.size(); field_idx++)
                {
                    if (r[field_idx] == 1)
                    {
                        break;
                    }
                }
                // std::cout << "rule " << idx << " is field " << field_idx <<
                // std::endl;

                // unset that field for all other rules
                for (auto [i2, r2] : possible)
                {
                    if (i2 != idx)
                    {
                        possible[i2][field_idx] = 0;
                    }
                }
            }
            else
            {
                done = false;
            }
        }
        if (done)
        {
            break;
        }
    }

    for (auto z = 0; z < 6; z++)
    {
        auto r = possible[z];
        for (field_idx = 0; field_idx < r.size(); field_idx++)
        {
            if (r[field_idx] == 1)
            {
                break;
            }
        }
        ans *= std::stol(my_ticket[field_idx]);
    }

    return ans;
}

int
main(int argc, char **argv)
{
    std::cout << part1() << "\n";
    std::cout << part2() << std::endl;
}
