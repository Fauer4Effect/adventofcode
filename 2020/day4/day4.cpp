#include "../split.h"
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <regex>

class Passport
{
  private:
    static bool verify_byr(std::string byr)
    {
        int year;
        try
        {
            year = std::stoi(byr);
        }
        catch (const std::exception &e)
        {
            return false;
        }
        return year >= 1920 && year <= 2002;
    }
    static bool verify_iyr(std::string iyr)
    {
        int year;
        try
        {
            year = std::stoi(iyr);
        }
        catch (const std::exception &e)
        {
            return false;
        }
        return year >= 2010 && year <= 2020;
    }
    static bool verify_eyr(std::string eyr)
    {
        int year;
        try
        {
            year = std::stoi(eyr);
        }
        catch (const std::exception &e)
        {
            return false;
        }
        return year >= 2020 && year <= 2030;
    }
    static bool verify_hgt(std::string hgt)
    {
        int height;
        try
        {
            height = std::stoi(hgt.substr(0, hgt.size() - 2));
        }
        catch (const std::exception &e)
        {
            return false;
        }
        if (!hgt.substr(hgt.size() - 2).compare("in"))
        {
            return height >= 59 && height <= 76;
        }
        else if (!hgt.substr(hgt.size() - 2).compare("cm"))
        {
            return height >= 150 && height <= 193;
        }
        else
        {
            return false;
        }
    }
    static bool verify_hcl(std::string hcl)
    {
        return std::regex_match(hcl, std::regex("^#[0-9a-f]{6}$"));
    }
    static bool verify_ecl(std::string ecl)
    {
        std::vector<std::string> valid{"amb", "blu", "brn", "gry",
                                       "grn", "hzl", "oth"};
        return std::find(valid.begin(), valid.end(), ecl) != valid.end();
    }
    static bool verify_cid(std::string cid) { return true; }
    static bool verify_pid(std::string pid)
    {
        return std::regex_match(pid, std::regex("^[0-9]{9}$"));
    }

  public:
    Passport()
    {
        verification_functions.emplace("byr", &verify_byr);
        verification_functions.emplace("iyr", &verify_iyr);
        verification_functions.emplace("eyr", &verify_eyr);
        verification_functions.emplace("hgt", &verify_hgt);
        verification_functions.emplace("hcl", &verify_hcl);
        verification_functions.emplace("ecl", &verify_ecl);
        verification_functions.emplace("cid", &verify_cid);
        verification_functions.emplace("pid", &verify_pid);
    }

    bool is_valid()
    {
        return fields["byr"] && fields["iyr"] && fields["eyr"] &&
               fields["hgt"] && fields["hcl"] && fields["ecl"] && fields["pid"];
    }

    void validate(std::string field, bool validate_fields)
    {
        std::vector<std::string> vals = split(field, ":");
        if (!validate_fields)
        {
            fields[vals[0]] = true;
        }
        else if (verification_functions[vals[0]](vals[1]))
        {
            fields[vals[0]] = true;
        }
    }

    std::map<std::string, bool> fields{
        {"byr", false}, {"iyr", false}, {"eyr", false}, {"hgt", false},
        {"hcl", false}, {"ecl", false}, {"cid", false}, {"pid", false}};

    std::map<std::string, std::function<bool(std::string)>>
        verification_functions{};
};

static int
check(bool validate_fields)
{
    std::fstream             my_input{"input.txt"};
    std::string              line;
    std::vector<std::string> fields;
    Passport                 passport{};
    int                      num_valid{};

    while (getline(my_input, line))
    {
        if (line.empty())
        {
            if (passport.is_valid())
            {
                num_valid++;
            }
            passport = Passport();
            continue;
        }

        fields = split(line, " ");
        for (auto field : fields)
        {
            passport.validate(field, validate_fields);
        }
    }
    return num_valid;
}

int
main(int argc, char **argv)
{
    std::cout << check(false) << std::endl;
    std::cout << check(true) << std::endl;
}