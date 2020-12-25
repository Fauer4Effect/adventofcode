#ifndef JOIN_H
#define JOIN_H

#include <sstream>

template <typename Iter>
std::string
join(Iter begin, Iter end, std::string const &sep)
{
    std::ostringstream res;
    if (begin != end)
    {
        res << *begin++;
    }
    while (begin != end)
    {
        res << sep << *begin++;
    }
    return res.str();
}

#endif // JOIN_H