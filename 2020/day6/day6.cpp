#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>

static int
part1()
{
    std::fstream     my_input{"input.txt"};
    std::string      line;
    std::set<char>   answers{};
    std::vector<int> count{};

    while (getline(my_input, line))
    {
        if (line.empty())
        {
            count.push_back(answers.size());
            answers.clear();
            continue;
        }
        for (auto question : line)
        {
            answers.insert(question);
        }
    }
    count.push_back(answers.size());
    return std::accumulate(count.begin(), count.end(), 0);
}

static void
setup_answer_map(std::map<char, int> &answers)
{
    std::string alphas = "abcdefghijklmnopqrstuvwxyz";
    for (char letter : alphas)
    {
        answers[letter] = 0;
    }
}

static int
part2()
{
    std::fstream        my_input{"input.txt"};
    std::string         line;
    std::map<char, int> answers{};
    std::vector<int>    count{};
    int                 group_size{};
    int                 total{};

    setup_answer_map(answers);
    while (getline(my_input, line))
    {
        if (line.empty())
        {
            for (auto question : answers)
            {
                if (question.second == group_size)
                {
                    total++;
                }
            }
            count.push_back(total);
            setup_answer_map(answers);
            group_size = 0;
            total      = 0;
            continue;
        }
        for (auto ans : line)
        {
            answers[ans]++;
        }
        group_size++;
    }

    for (auto question : answers)
    {
        if (question.second == group_size)
        {
            total++;
        }
    }
    count.push_back(total);

    return std::accumulate(count.begin(), count.end(), 0);
}

int
main(int argc, char **argv)
{
    std::cout << part1() << '\n';
    std::cout << part2() << std::endl;
}