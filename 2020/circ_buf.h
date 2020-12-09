#include <cstddef>
#include <mutex>

template <class T> class circular_buffer
{
  public:
    explicit circular_buffer(size_t size) : max_size_(size)
    {
        buf_ = new T[max_size_];
    }

    class iterator
    {
      public:
        typedef iterator                  self_type;
        typedef T                         value_type;
        typedef T &                       reference;
        typedef T *                       pointer;
        typedef std::forward_iterator_tag iterator_category;
        typedef int                       difference_type;
        iterator(pointer ptr) : ptr_(ptr) {}
        self_type operator++()
        {
            self_type i = *this;
            ptr_++;
            return i;
        }
        self_type operator++(int junk)
        {
            ptr_++;
            return *this;
        }
        reference operator*() { return *ptr_; }
        pointer   operator->() { return ptr_; }
        bool      operator==(const self_type &rhs) { return ptr_ == rhs.ptr_; }
        bool      operator!=(const self_type &rhs) { return ptr_ != rhs.ptr_; }

      private:
        pointer ptr_;
    };

    class const_iterator
    {
      public:
        typedef const_iterator            self_type;
        typedef T                         value_type;
        typedef T &                       reference;
        typedef T *                       pointer;
        typedef int                       difference_type;
        typedef std::forward_iterator_tag iterator_category;
        const_iterator(pointer ptr) : ptr_(ptr) {}
        self_type operator++()
        {
            self_type i = *this;
            ptr_++;
            return i;
        }
        self_type operator++(int junk)
        {
            ptr_++;
            return *this;
        }
        const reference operator*() { return *ptr_; }
        const pointer   operator->() { return ptr_; }
        bool operator==(const self_type &rhs) { return ptr_ == rhs.ptr_; }
        bool operator!=(const self_type &rhs) { return ptr_ != rhs.ptr_; }

      private:
        pointer ptr_;
    };

    iterator       begin() { return iterator(buf_); }
    iterator       end() { return iterator(buf_ + size()); }
    const_iterator begin() const { return const_iterator(buf_); }
    const_iterator end() const { return const_iterator(buf_ + size()); }

    void put(T item)
    {
        std::lock_guard<std::mutex> lock(mutex_);
        buf_[head_] = item;
        if (full_)
        {
            tail_ = (tail_ + 1) % max_size_;
        }
        head_ = (head_ + 1) % max_size_;
        full_ = head_ == tail_;
    }
    T get()
    {
        std::lock_guard<std::mutex> lock(mutex_);
        if (empty())
        {
            return T();
        }
        auto val = buf_[tail_];
        full_    = false;
        tail_    = (tail_ + 1) % max_size_;

        return val;
    }
    void reset()
    {
        std::lock_guard<std::mutex> lock(mutex_);
        head_ = tail_;
        full_ = false;
    }
    bool empty() const { return (!full_ && (head_ == tail_)); }
    bool full() const { return full_; }
    bool contains(T item) const
    {
        if (!empty())
        {
            for (size_t i = 0; i < max_size_; i++)
            {
                if (item == buf_[i])
                {
                    return true;
                }
            }
        }
        return false;
    }
    size_t capacity() const { return max_size_; }
    size_t size() const
    {
        size_t size = max_size_;
        if (!full_)
        {
            if (head_ >= tail_)
            {
                size = head_ - tail_;
            }
            else
            {
                size = max_size_ + head_ - tail_;
            }
        }
        return size;
    }

  private:
    std::mutex   mutex_;
    T *          buf_;
    size_t       head_ = 0;
    size_t       tail_ = 0;
    const size_t max_size_;
    bool         full_ = 0;
};