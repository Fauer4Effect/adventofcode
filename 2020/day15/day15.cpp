#include "../split.h"
#include "robin_hood.h"
#include <fstream>
#include <iostream>

class Num
{
  public:
    Num() {}
    Num(int turn) : last_spoken{turn}, time_before{}, first_time{true} {}

    int  last_spoken;
    int  time_before;
    bool first_time;
};

static long
spoken_num(long index)
{
    std::fstream                              my_input{"input.txt"};
    std::string                               line;
    robin_hood::unordered_flat_map<long, Num> spoken{};
    std::vector<std::string>                  starts;
    long                                      cur_turn{1};
    long                                      last_spoken{};

    getline(my_input, line);
    starts = split(line, ",");

    for (auto starter : starts)
    {
        spoken[std::stol(starter)] = Num(cur_turn++);
    }
    last_spoken = std::stol(starts.back());

    while (cur_turn <= index)
    {
        // std::cout << cur_turn << " " << last_spoken << std::endl;
        if (spoken[last_spoken].first_time)
        {
            last_spoken   = 0;
            Num &n        = spoken[last_spoken];
            n.time_before = n.last_spoken;
            n.last_spoken = cur_turn++;
            n.first_time  = false;
        }
        else
        {
            last_spoken = spoken[last_spoken].last_spoken -
                          spoken[last_spoken].time_before;
            if (spoken.end() != spoken.find(last_spoken))
            {
                Num &n        = spoken[last_spoken];
                n.time_before = n.last_spoken;
                n.last_spoken = cur_turn++;
                n.first_time  = false;
            }
            else
            {
                spoken[last_spoken] = Num(cur_turn++);
            }
        }
    }
    return last_spoken;
}

int
main(int argc, char **argv)
{
    std::cout << spoken_num(2020) << "\n";
    std::cout << spoken_num(30000000) << std::endl;
}
