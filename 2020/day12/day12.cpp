#include <algorithm>
#include <fstream>
#include <iostream>

// From a quick peek at the input we realize that the turning movements are
// always given by 90 degrees
std::pair<int, int>
make_cartestian(int r, int theta)
{
    std::pair<int, int> res;
    switch (theta)
    {
    case 0:
        res = std::make_pair(r, 0);
        break;
    case 90:
        res = std::make_pair(0, r);
        break;
    case 180:
        res = std::make_pair(-r, 0);
        break;
    case 270:
        res = std::make_pair(0, -r);
        break;
    }
    return res;
}

std::pair<int, int>
rotate(int x, int y, int angle)
{
    std::pair<int, int> res;
    switch (angle)
    {
    case 0:
        res = std::make_pair(x, y);
        break;
    case 90:
        res = std::make_pair(-y, x);
        break;
    case 180:
        res = std::make_pair(-x, -y);
        break;
    case 270:
        res = std::make_pair(y, -x);
        break;
    }
    return res;
}

static int
mod(int a, int b)
{
    return (a % b + b) % b;
}

static int
part1()
{
    std::fstream        my_input{"input.txt"};
    std::string         line;
    std::pair<int, int> move;
    int                 cur_angle{};
    int                 cur_x{};
    int                 cur_y{};
    int                 val;

    while (getline(my_input, line))
    {
        val = std::stoi(line.substr(1));
        switch (line[0])
        {
        case 'N':
            cur_y += val;
            break;
        case 'S':
            cur_y -= val;
            break;
        case 'E':
            cur_x += val;
            break;
        case 'W':
            cur_x -= val;
            break;
        case 'L':
            cur_angle += val;
            cur_angle = mod(cur_angle, 360);
            break;
        case 'R':
            cur_angle -= val;
            cur_angle = mod(cur_angle, 360);
            break;
        case 'F':
            move = make_cartestian(val, cur_angle);
            cur_x += move.first;
            cur_y += move.second;
            break;
        }
    }

    return std::abs(cur_x) + std::abs(cur_y);
}

static int
part2()
{
    std::fstream        my_input{"input.txt"};
    std::string         line;
    std::pair<int, int> moved;
    int                 ship_x{};
    int                 ship_y{};
    int                 way_x{10};
    int                 way_y{1};
    int                 val;

    while (getline(my_input, line))
    {
        val = std::stoi(line.substr(1));
        switch (line[0])
        {
        case 'N':
            way_y += val;
            break;
        case 'S':
            way_y -= val;
            break;
        case 'E':
            way_x += val;
            break;
        case 'W':
            way_x -= val;
            break;
        case 'L':
            moved = rotate(way_x, way_y, val);
            way_x = moved.first;
            way_y = moved.second;
            break;
        case 'R':
            moved = rotate(way_x, way_y, mod(-val, 360));
            way_x = moved.first;
            way_y = moved.second;
            break;
        case 'F':
            ship_x += val * way_x;
            ship_y += val * way_y;
            break;
        }
    }
    return std::abs(ship_x) + std::abs(ship_y);
}

int
main(int argc, char **argv)
{
    std::cout << part1() << "\n";
    std::cout << part2() << std::endl;
}