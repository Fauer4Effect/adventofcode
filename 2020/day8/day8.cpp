#include <bitset>
#include <fstream>
#include <iostream>
#include <vector>

static int
parse_input(std::vector<std::string> &boot)
{
    std::fstream my_input{"input.txt"};
    std::string  line;
    int          lines{};
    while (getline(my_input, line))
    {
        boot.push_back(line);
        lines++;
    }
    return lines;
}

static void
do_inst(int &accum, int &rip, std::string inst)
{
    int operand;
    switch (inst[0])
    {
    case 'n':
        rip++;
        break;
    case 'a':
        operand = std::stoi(inst.substr(5, std::string::npos));
        accum += ('+' == inst[4]) ? operand : (0 - operand);
        rip++;
        break;
    case 'j':
        operand = std::stoi(inst.substr(5, std::string::npos));
        rip += ('+' == inst[4]) ? operand : (0 - operand);
        break;
    default:
        break;
    }
}

static int
part1()
{
    std::vector<std::string> boot{};
    std::string              inst;
    std::bitset<1000>        execd;
    int                      rip{};
    int                      accum{};

    parse_input(boot);
    while (1)
    {
        if (execd[rip])
        {
            break;
        }
        execd.set(rip);
        inst = boot[rip];
        do_inst(accum, rip, inst);
    }
    return accum;
}

static int
part2()
{
    std::vector<std::string> boot{};
    std::string              inst;
    std::bitset<1000>        execd;
    int                      rip;
    int                      accum;
    int                      lines;
    int                      modified;
    bool                     loop;

    lines = parse_input(boot);
    for (modified = 0; modified < lines; modified++)
    {
        accum = 0;
        rip   = 0;
        execd.reset();
        loop = false;
        while (rip < lines)
        {
            if (execd[rip])
            {
                loop = true;
                break;
            }
            execd.set(rip);
            inst = boot[rip];
            if (inst[0] != 'a' && rip == modified)
            {
                inst[0] = (inst[0] == 'n') ? 'j' : 'n';
            }
            do_inst(accum, rip, inst);
        }
        if (!loop)
        {
            break;
        }
    }
    return accum;
}

int
main(int argc, char **argv)
{
    std::cout << part1() << "\n";
    std::cout << part2() << std::endl;
}