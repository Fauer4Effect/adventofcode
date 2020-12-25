#include "../robin_hood.h"
#include "../split.h"
#include <fstream>
#include <iostream>
#include <regex>
#include <string>

std::string
build_re(robin_hood::unordered_flat_map<std::string, std::string> &rules,
         std::string                                               index)
{
    if (!rules[index].compare("a") || !rules[index].compare("b"))
    {
        return rules[index];
    }

    std::string rx{"("};
    for (auto s : split(rules[index], " "))
    {
        if (!s.compare("|"))
        {
            rx += s;
        }
        else
        {
            rx += build_re(rules, s);
        }
    }
    rx += ")";
    return rx;
}

static int
part1()
{
    std::fstream             my_input{"input.txt"};
    std::vector<std::string> splits;
    robin_hood::unordered_flat_map<std::string, std::string> rules;
    std::string                                              line;
    std::string                                              rule_num;
    std::regex                                               re;
    int                                                      valid{};

    // Get rules
    getline(my_input, line);
    while (!line.empty())
    {
        splits   = split(line, ": ");
        rule_num = splits[0];
        if (splits[1].find("a") != std::string::npos)
        {
            rules[rule_num] = std::string{"a"};
        }
        else if (splits[1].find("b") != std::string::npos)
        {
            rules[rule_num] = std::string{"b"};
        }
        else
        {
            rules[rule_num] = splits[1];
        }
        getline(my_input, line);
    }

    re = std::regex(build_re(rules, "0"));

    while (getline(my_input, line))
    {
        if (std::regex_match(line.begin(), line.end(), re))
        {
            valid++;
        }
    }
    return valid;
}

static int
part2()
{
    robin_hood::unordered_flat_map<std::string, std::string> rules;
    std::fstream             my_input{"input.txt"};
    std::vector<std::string> splits;
    std::string              line;
    std::string              rule_num;
    std::string              rule_42;
    std::string              rule_31;
    std::regex               p2;
    int                      i;
    int                      valid{};
    bool                     done{false};

    // from the input we see that 0: 8 11
    // this one has loops 8: 42 | 42 8
    // 11: 42 31 | 42 11 31
    // if we skip that first loop we can resolve the regex for
    // 42 and 31
    // Simplest case with no loop
    //
    // 42 42 31         we see here that there are 2x 42 and 1x 31
    // 8 loops one time
    // 42 42 42 31      here there are 3x 42 and 1x 31
    // 11 loops one time
    // 42 42 42 31 31   here 3x 42 and 2x 31
    // 11 loops 2 times
    // 42 42 42 42 31 31 31 4x 42 and 3x 31
    // there always will be at least one additional 42

    // Get rules
    getline(my_input, line);
    while (!line.empty())
    {
        splits   = split(line, ": ");
        rule_num = splits[0];
        if (splits[1].find("a") != std::string::npos)
        {
            rules[rule_num] = std::string{"a"};
        }
        else if (splits[1].find("b") != std::string::npos)
        {
            rules[rule_num] = std::string{"b"};
        }
        else
        {
            rules[rule_num] = splits[1];
        }
        getline(my_input, line);
    }

    // resolve the nonlooping sub rules
    rule_42 = build_re(rules, "42");
    rule_31 = build_re(rules, "31");

    // get the inputs
    splits.clear();
    while (getline(my_input, line))
    {
        splits.push_back(line);
    }

    // start at 1 because we always need to have at least 1 occurence of each
    // just keep looping until we have a big neough size to cover all inputs
    i = 1;
    while (!done)
    {
        done = true;
        // You will always have more of rule_42 than rule_31
        // so you can't do rule_31+ because then that won't be constrained
        // by the number of rule_42
        p2 =
            std::regex("^" + rule_42 + "+" + rule_42 + "{" + std::to_string(i) +
                       "}" + rule_31 + "{" + std::to_string(i) + "}$");

        for (auto s : splits)
        {
            if (std::regex_match(s.begin(), s.end(), p2))
            {
                valid++;
                done = false;
            }
        }

        i++;
    }

    return valid;
}

int
main(int argc, char **arv)
{
    std::cout << part1() << "\n";
    std::cout << part2() << std::endl;
}
