#include <cstdint>
#include <fstream>
#include <iostream>
#include <unordered_set>
#include <vector>

class Tile;

using char_matrix_t = std::vector<std::vector<char>>;
using tile_matrix_t = std::vector<std::vector<Tile *>>;

static char_matrix_t
do_rotate(const char_matrix_t &matrix)
{
    char_matrix_t out = matrix;
    for (auto r = 0; r < matrix.size(); r++)
    {
        for (auto c = 0; c < matrix.size(); c++)
        {
            auto new_r        = c;
            auto new_c        = matrix.size() - 1 - r;
            out[new_r][new_c] = matrix[r][c];
        }
    }
    return out;
}

static char_matrix_t
do_flip(const char_matrix_t &matrix)
{
    char_matrix_t out = matrix;
    for (auto r = 0; r < matrix.size(); r++)
    {
        for (auto c = 0; c < matrix.size(); c++)
        {
            auto new_r        = r;
            auto new_c        = matrix.size() - 1 - c;
            out[new_r][new_c] = matrix[r][c];
        }
    }
    return out;
}

class Tile
{
  public:
    Tile() {}

    void calc_versions()
    {
        versions.push_back(do_rotate(this->contents));
        versions.push_back(do_rotate(this->versions.back()));
        versions.push_back(do_rotate(this->versions.back()));
        versions.push_back(do_rotate(this->versions.back()));

        versions.push_back(do_flip(this->contents));
        versions.push_back(do_rotate(this->versions.back()));
        versions.push_back(do_rotate(this->versions.back()));
        versions.push_back(do_rotate(this->versions.back()));
    }

    int                        num{};
    int                        matching_version{};
    int                        actual_version{};
    char_matrix_t              contents{};
    std::vector<char_matrix_t> versions;
};

static bool
check_left_fit(const Tile &l, const Tile &r)
{
    char_matrix_t lv  = l.versions[l.actual_version];
    char_matrix_t rv  = r.versions[r.actual_version];
    std::size_t   len = lv[0].size();
    for (auto ri = 0; ri < len; ri++)
    {
        if (lv[ri][len - 1] != rv[ri][0])
        {
            return false;
        }
    }
    return true;
}

static bool
check_top_fit(const Tile &top, const Tile &bot)
{
    char_matrix_t tv  = top.versions[top.actual_version];
    char_matrix_t bv  = bot.versions[bot.actual_version];
    std::size_t   len = tv[0].size();
    for (auto ci = 0; ci < len; ci++)
    {
        if (tv[len - 1][ci] != bv[0][ci])
        {
            return false;
        }
    }
    return true;
}

static bool
check_tile(std::vector<Tile> &tiles, std::unordered_set<int> &in_use,
           tile_matrix_t &matrix, std::size_t row, std::size_t col,
           std::size_t dimensions)
{
    // 1. Find a tile that is not in use
    // 2. Place that tile into the open spot in the matrix
    // 3. check if the tile has an orientation that matches the tiles left/top
    // of it
    // Go through all orientations
    // Check if it fits left/top
    // if it does then recurssively check the next (bottom and right)
    // tile and see if there is one that will fit there
    // if one does then we have a good fit, confirm location and orientation
    // if nothing matches then we need to keep checking
    // if there is not match remove from in use, remove from matrix, and restart
    // 4. if no matching tile can be found, remove from in use and matrix and
    // return failure
    if (row >= dimensions || col >= dimensions)
    {
        return true;
    }

    for (auto &tile : tiles)
    {
        if (in_use.find(tile.num) != in_use.end())
        {
            continue;
        }

        in_use.insert(tile.num);
        matrix[row][col] = &tile;

        for (auto vi = 0; vi < tile.versions.size(); vi++)
        {
            tile.actual_version = vi;
            bool left_fit       = true;
            bool top_fit        = true;
            if (col > 0)
            {
                left_fit = check_left_fit(*matrix[row][col - 1], tile);
            }
            if (row > 0)
            {
                top_fit = check_top_fit(*matrix[row - 1][col], tile);
            }

            if (left_fit && top_fit)
            {
                auto next_col = (col + 1) % dimensions;
                auto next_row = (dimensions * row + col + 1) / dimensions;
                if (check_tile(tiles, in_use, matrix, next_row, next_col,
                               dimensions))
                {
                    tile.matching_version = vi;
                    return true;
                }
            }
            tile.actual_version = -1;
        }
        matrix[row][col] = nullptr;
        in_use.erase(tile.num);
    }

    return false;
}

static tile_matrix_t
resolve_matrix(std::vector<Tile> &tiles, tile_matrix_t &matrix,
               std::size_t dimensions)
{
    std::fstream            my_input{"input.txt"};
    std::string             line;
    std::vector<Tile *>     row;
    std::unordered_set<int> in_use;
    Tile                    cur;

    while (getline(my_input, line))
    {
        if (line.empty())
        {
            cur.calc_versions();
            tiles.push_back(cur);
        }
        else if (line.find("T") != std::string::npos)
        {
            cur     = Tile();
            cur.num = std::stoi(line.substr(5, line.size() - 1));
        }
        else
        {
            cur.contents.push_back(std::vector<char>(line.begin(), line.end()));
        }
    }
    cur.calc_versions();
    tiles.push_back(cur);

    // std::cout << tiles.size() << std::endl;
    for (auto i = 0; i < dimensions; i++)
    {
        row = std::vector<Tile *>();
        for (auto j = 0; j < dimensions; j++)
        {
            row.push_back(nullptr);
        }
        matrix.push_back(row);
    }

    check_tile(tiles, in_use, matrix, 0, 0, dimensions);
    return matrix;
}

static std::uint64_t
part1(const tile_matrix_t &matrix, std::size_t dimensions)
{
    std::uint64_t ans{1};

    ans *= matrix[0][0]->num;
    ans *= matrix[0][dimensions - 1]->num;
    ans *= matrix[dimensions - 1][0]->num;
    ans *= matrix[dimensions - 1][dimensions - 1]->num;

    return ans;
}

static int mark_monster(char_matrix_t &image, const std::vector<std::pair<int, int>> &monster_coords)
{
    int monsters{};
    int new_r;
    int new_c;
    bool has_monster;

    for (auto r = 0; r < image.size(); r++)
    {
        for (auto c = 0; c < image[r].size(); c++)
        {
            has_monster = true;
            for (auto [x, y] : monster_coords)
            {
                new_r = r + x;
                new_c = c + y;
                if (new_r >= image.size() || new_c >= image[r].size())
                {
                    has_monster = false;
                    break;
                }
                if (image[new_r][new_c] != '#')
                {
                    has_monster = false;
                    break;
                }
            }
            if (has_monster)
            {
                monsters++;
                for (auto [x, y] : monster_coords)
                {
                    new_r = r+x;
                    new_c = c + y;
                    image[new_r][new_c] = '0';
                }
            }
        }
    }

    return monsters;
}

static std::uint64_t get_roughness(const char_matrix_t &image)
{
    std::uint64_t rough{};
    for (auto r : image)
    {
        for (auto c : r)
        {
            if ('#' == c)
            {
                rough++;
            }
        }
    }
    return rough;
}

static void print_image(char_matrix_t& image)
{
    for (auto r : image)
    {
        for (auto c : r)
        {
            std::cout << c;
        }
        std::cout << "\n";
    }
}

static std::uint64_t
part2(tile_matrix_t &matrix, std::size_t dimensions)
{
    char_matrix_t                    image{};
    char_matrix_t                    pixels;
    std::vector<std::pair<int, int>> monster_coords{
        {0, 18}, {1, 0}, {1, 5}, {1, 6}, {1, 11}, {1, 12}, {1, 17}, {1, 18},
        {1, 19}, {2, 1}, {2, 4}, {2, 7}, {2, 10}, {2, 13}, {2, 16}};
    std::size_t width;
    std::size_t len;
    int new_r;
    int new_c;
    int num_monsters{};
    int transformation{};
    std::uint64_t roughness{};

    // first we have to remove all the borders from the image
    width = matrix.size() * (matrix[0][0]->contents.size() - 2);
    for (auto r = 0; r < width; r++)
    {
        image.push_back(std::vector<char>(width, 0));
    }
    for (auto r = 0; r < matrix.size(); r++)
    {
        for (auto c = 0; c < matrix[0].size(); c++)
        {
            pixels = matrix[r][c]->versions[matrix[r][c]->matching_version];
            len = pixels.size() - 2;
            for (auto r2 = 1; r2 < pixels.size()-1; r2++)
            {
                for (auto c2=1; c2 < pixels.size()-1; c2++)
                {
                    new_r = r * len + r2 - 1;
                    new_c = c * len + c2 - 1;
                    image[new_r][new_c] = pixels[r2][c2];
                }
            }
        }
    }

    // now we have to find the one orientation that actually has sea monsters
    // then once we have that we can mark all the sea monsters
    // and then we can count up what is left
    while (!num_monsters)
    {
        num_monsters = mark_monster(image, monster_coords);
        if (num_monsters)
        {
            roughness = get_roughness(image);
            for (auto r : image)
            {
                for (auto c : r)
                {
                    std::cout << c;
                }
                std::cout << "\n";
            }
            break;
        }
        if (transformation < 4)
        {
            image = do_rotate(image);
            transformation++;
        }
        else
        {
            transformation = 0;
            image = do_flip(image);
        }
        
    }
    return roughness;
}

int
main(int argc, char **argv)
{
    int           dimensions{12};
    std::vector<Tile> tiles;
    tile_matrix_t     matrix{};
    matrix = resolve_matrix(tiles, matrix, dimensions);

    std::cout << part1(matrix, dimensions) << "\n";
    std::cout << part2(matrix, dimensions) << std::endl;
}
