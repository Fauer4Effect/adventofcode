#include <bitset>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <vector>

static void
generate_bin_str(std::vector<std::string> &buf, std::string value, int i)
{
    if (i == value.size())
    {
        buf.push_back(value);
        return;
    }
    if ('X' != value[i])
    {
        generate_bin_str(buf, value, i + 1);
        return;
    }

    value[i] = '0';
    generate_bin_str(buf, value, i + 1);

    value[i] = '1';
    generate_bin_str(buf, value, i + 1);
}

static long
part1()
{
    std::fstream                  my_input{"input.txt"};
    std::string                   line;
    std::string                   mask{"0", 36};
    std::unordered_map<int, long> mem{};
    long                          sum{};
    int                           start;
    int                           end;
    int                           index;
    std::bitset<36>               value;

    while (getline(my_input, line))
    {
        if ('a' == line[1])
        {
            start = line.find("=");
            mask  = line.substr(start + 2);
        }
        else
        {
            start = line.find("[");
            end   = line.find("]");
            index = std::stoi(line.substr(start + 1, end));
            start = line.find("=");
            value = std::bitset<36>(std::stol(line.substr(start + 2)));
            for (auto i = 0; i < mask.size(); i++)
            {
                if ('0' == mask[i])
                {
                    value.reset(36 - i - 1);
                }
                else if ('1' == mask[i])
                {
                    value.set(36 - i - 1);
                }
            }
            mem[index] = value.to_ulong();
        }
    }

    for (auto p : mem)
    {
        sum += p.second;
    }
    return sum;
}

static long
part2()
{
    std::fstream                   my_input{"input.txt"};
    std::string                    line;
    std::string                    mask{"0", 36};
    std::unordered_map<long, long> mem{};
    std::vector<std::string>       addrs;
    std::bitset<36>                index;
    std::string                    address;
    long                           sum{};
    int                            start;
    int                            end;
    long                           value;

    while (getline(my_input, line))
    {
        if ('a' == line[1])
        {
            start = line.find("=");
            mask  = line.substr(start + 2);
        }
        else
        {
            start   = line.find("[");
            end     = line.find("]");
            index   = std::bitset<36>(std::stol(line.substr(start + 1, end)));
            address = index.to_string();

            start = line.find("=");
            value = std::stol(line.substr(start + 2));
            for (auto i = 0; i < mask.size(); i++)
            {
                if ('X' == mask[i])
                {
                    address[i] = 'X';
                }
                else if ('1' == mask[i])
                {
                    address[i] = '1';
                }
            }
            generate_bin_str(addrs, address, 0);
            for (auto addr : addrs)
            {
                mem[std::stol(addr, 0, 2)] = value;
            }
            addrs.clear();
        }
    }

    for (auto p : mem)
    {
        sum += p.second;
    }
    return sum;
}

int
main(int argc, char **argv)
{
    std::cout << part1() << "\n";
    std::cout << part2() << std::endl;
}
