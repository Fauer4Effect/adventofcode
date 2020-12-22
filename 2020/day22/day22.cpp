#include <fstream>
#include <iostream>
#include <deque>
#include <unordered_set>
#include <sstream>
#include <utility>

using pair = std::pair<std::string, std::string>;
 
struct pair_hash
{
    template <class T1, class T2>
    std::size_t operator() (const std::pair<T1, T2> &pair) const
    {
        return std::hash<T1>()(pair.first) ^ std::hash<T2>()(pair.second);
    }
};

static std::uint64_t part1()
{
    std::fstream my_input{"input.txt"};
    std::string line;
    std::deque<int> player1{};
    std::deque<int> player2{};
    int c1;
    int c2;
    std::uint64_t score{};

    getline(my_input, line);        // throw away player name
    getline(my_input, line);
    while (!line.empty())
    {
        player1.push_back(std::stoi(line));
        getline(my_input, line);
    }

    getline(my_input, line);
    getline(my_input, line);
    while (!line.empty())
    {
        player2.push_back(std::stoi(line));
        getline(my_input, line);
    }

    while (player1.size() != 0 && player2.size() != 0)
    {
        c1 = player1.front();
        player1.pop_front();
        c2 = player2.front();
        player2.pop_front();

        if (c1 > c2)
        {
            player1.push_back(c1);
            player1.push_back(c2);
        }
        else if (c2 > c1)
        {
            player2.push_back(c2);
            player2.push_back(c1);
        }
    }

    if (player1.size() == 0)
    {
        for (auto i = 1; i < player2.size(); i++)
        {
            score += player2[player2.size()-i] * i;
        }
        score += player2[0] * player2.size();
    }
    else if (player2.size() == 0)
    {
        for (auto i = 1; i < player1.size(); i++)
        {
            score += player1[player1.size()-i] * i;
        }
        score += player1[0] * player1.size();
    }
    
    return score;
}

static std::string deck_2_str(std::deque<int> deck)
{
    std::ostringstream out{};
    for (auto c : deck)
    {
        out << c;
    }
    return out.str();
}

// retun 1 if player 1 wins return -1 if player 2 wins
static int play_combat(std::deque<int>& player1, std::deque<int>& player2, std::unordered_set<pair, pair_hash>& previous)
{
    std::string player1_str;
    std::string player2_str;
    pair cur_game;
    int c1;
    int c2;
    int winner;

    

    while(player1.size() != 0 && player2.size() != 0)
    {
        player1_str = deck_2_str(player1);
        player2_str = deck_2_str(player2);
        cur_game = std::make_pair(player1_str, player2_str);
        if (previous.find(cur_game) != previous.end())
        {
            // player 1 wins
            return 1;
        }
        previous.insert(cur_game);

        c1 = player1.front();
        player1.pop_front();
        c2 = player2.front();
        player2.pop_front();

        if (c1 <= player1.size() && c2 <= player2.size())
        {
            auto tmp1 = std::deque<int>();
            for (auto i = 0; i < c1; i++)
            {
                tmp1.push_back(player1[i]);
            }
            auto tmp2 = std::deque<int>();
            for (auto i = 0; i < c2; i++)
            {
                tmp2.push_back(player2[i]);
            }
            auto tmp_r = previous;
            winner = play_combat(tmp1, tmp2, tmp_r);
        }
        else
        {
            if (c1 > c2)
            {
                winner = 1;
            }
            else
            {
                winner = -1;
            }
        }
        
        if (1 == winner)
        {
            player1.push_back(c1);
            player1.push_back(c2);
        }
        else
        {
            player2.push_back(c2);
            player2.push_back(c1);
        }
    }
    
    return winner;
}

static std::uint64_t part2()
{
    std::fstream my_input{"input.txt"};
    std::string line;
    std::deque<int> player1{};
    std::deque<int> player2{};
    // set of deck configurations from previous games
    // TODO need to replace this with custom implementation that
    // allows for pair keys
    std::unordered_set<pair, pair_hash> previous_games{};
    int winner;
    std::uint64_t score{};

    getline(my_input, line);        // throw away player name
    getline(my_input, line);
    while (!line.empty())
    {
        player1.push_back(std::stoi(line));
        getline(my_input, line);
    }

    getline(my_input, line);
    getline(my_input, line);
    while (!line.empty())
    {
        player2.push_back(std::stoi(line));
        getline(my_input, line);
    }

    winner = play_combat(player1, player2, previous_games);
    if (1 == winner)
    {
        for (auto i = 1; i < player1.size(); i++)
        {
            score += player1[player1.size()-i] * i;
        }
        score += player1[0] * player1.size();
    }
    else
    {
        for (auto i = 1; i < player2.size(); i++)
        {
            score += player2[player2.size()-i] * i;
        }
        score += player2[0] * player2.size();
    }
    return score;
}

int main(int argc, char **argv)
{
    std::cout << part1() << "\n";
    std::cout << part2() << std::endl;
}
