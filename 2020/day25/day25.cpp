#include <iostream>

static size_t
get_loop_size(uint64_t key, uint64_t subject_num)
{
    uint64_t val{1};
    size_t   loop_size{};
    while (val != key)
    {
        val *= subject_num;
        val %= 20201227;
        loop_size++;
    }

    return loop_size;
}

static uint64_t
part1()
{
    uint64_t door_key{9789649};
    uint64_t card_key{3647239};
    uint64_t subject_num{7};
    uint64_t val{1};
    size_t   door_loop_size{};
    size_t   card_loop_size{};

    door_loop_size = get_loop_size(door_key, subject_num);
    card_loop_size = get_loop_size(card_key, subject_num);

    for (auto i = 0; i < door_loop_size; i++)
    {
        val *= card_key;
        val %= 20201227;
    }

    return val;
}

int
main(int argc, char **argv)
{
    std::cout << part1() << std::endl;
}
