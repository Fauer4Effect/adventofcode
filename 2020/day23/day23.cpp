#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <sstream>
#include <vector>

static std::string
part1()
{
    // Instead of worrying about keeping the circular buffer in order
    // and progressing the current index through the circle
    // We will just keep the current index to be index 1 in the buffer
    // and when we re-construct after each move we will just keep the
    // cups in that absolute order.
    size_t num_cups  = 9;
    size_t num_turns = 100;
    // We have to rotate the starting position by 1 since we choose
    // the current cup to be at index 1
    // std::vector<int> cups{7, 3, 8, 9, 1, 2, 5, 4,6};
    std::vector<int>   cups{2, 1, 5, 8, 9, 3, 7, 4, 6};
    std::vector<int>   picked;
    std::vector<int>   tmp;
    int                lo = 1;
    int                hi = 9;
    int                cur;
    int                dest;
    int                i_pos;
    std::ostringstream out;

    for (auto turn = 0; turn < num_turns; turn++)
    {
        cur = cups[1];
        picked.clear();
        picked.push_back(cups[2]);
        picked.push_back(cups[3]);
        picked.push_back(cups[4]);

        dest = (cur - 1 >= lo) ? (cur - 1) : hi;
        while (std::find(picked.begin(), picked.end(), dest) != picked.end())
        {
            dest = (dest - 1 >= lo) ? (dest - 1) : hi;
        }

        tmp.clear();
        for (auto j = 1; j < num_cups + 1; j++)
        {
            auto c = cups[j % num_cups];
            tmp.push_back(c);
            if (cur == c)
            {
                j += 3;
            }
            else if (dest == c)
            {
                for (auto cu : picked)
                {
                    tmp.push_back(cu);
                }
            }
        }
        cups = tmp;
    }

    i_pos = 0;
    while (true)
    {
        if (1 != cups[i_pos])
        {
            i_pos++;
        }
        else
        {
            for (auto j = i_pos + 1; j < num_cups; j++)
            {
                out << cups[j];
            }
            for (auto j = 0; j < i_pos; j++)
            {
                out << cups[j];
            }
            break;
        }
    }
    return out.str();
}

static uint64_t
part2()
{
    // my input : 158937462
    std::string        input = "158937462";
    std::unordered_map<int, int> cups{{1, 5}, {5, 8}, {8, 9}, {9, 3}, {3, 7},
                            {7, 4}, {4, 6}, {6, 2}, {2, 10}};
    std::vector<int>   skipped;
    int                num_cups{1000000};
    int                num_turns{10000000};
    int                cur;

    for (auto c = 10; c < num_cups; c++)
    {
        cups[c] = c + 1;
    }
    cups[num_cups] = 1;

    cur = 1;
    for (auto turn = 0; turn < num_turns; turn++)
    {
        int first_skipped  = cups[cur];
        int second_skipped = cups[first_skipped];
        int last_skipped   = cups[second_skipped];
        int after_skipped  = cups[last_skipped];

        skipped.clear();
        skipped.push_back(first_skipped);
        skipped.push_back(second_skipped);
        skipped.push_back(last_skipped);

        int dest = (cur - 1 >= 1) ? (cur - 1) : num_cups;
        while (std::find(skipped.begin(), skipped.end(), dest) != skipped.end())
        {
            dest = (dest - 1 >= 1) ? (dest - 1) : num_cups;
        }

        int after_dest = cups[dest];

        cups[cur]          = after_skipped;
        cups[dest]         = first_skipped;
        cups[last_skipped] = after_dest;
        cur                = cups[cur];
    }

    uint64_t c1 = cups[1];
    uint64_t c2 = cups[c1];
    return c1 * c2;
}

int
main(int argc, char **argv)
{
    std::cout << part1() << "\n";
    std::cout << part2() << std::endl;
}
