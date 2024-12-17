#include <iostream>
#include <cstdint>

#include <thread>

static constexpr int THREAD_COUNT = 16;
static constexpr int64_t CASES_PER_THREAD = ((1ll << 32) / THREAD_COUNT);

static const int8_t program[] = { 2,4,1,2,7,5,1,3,4,4,5,5,0,3,3,0 };

bool do_simulate(int64_t initval, int64_t expectedval) 
{
    int64_t A = initval;
    int64_t B = 0;
    int64_t C = 0;

    int64_t out = 0;
    int outcount = 0;

    for (int pc = 0; pc < sizeof(program); pc += 2) 
    {
        int8_t op = program[pc];
        int8_t literal = program[pc + 1];
        int64_t combo = literal;
        switch (literal) 
        {
            case 4:
                combo = A;
                break;
            case 5:
                combo = B;
                break;
            case 6:
                combo = C;
                break;
        }

        switch (op) 
        {
            case 0:
                A >>= combo;
                break;
            case 1:
                B ^= literal;
                break;
            case 2:
                B &= 0b111;
                break;
            case 3:
                if (A) 
                {
                    pc = literal - 2;
                }
                break;
            case 4:
                B ^= C;
                break;
            case 5:
                out <<= 3;
                out |= combo & 0b111;
                outcount++;

                if (outcount > sizeof(program) || out != (expectedval >> (3 * (sizeof(program) - outcount)))) 
                {
                    return false;
                }
                break;
            case 6:
                B = A >> combo;
                break;
            case 7:
                C = A >> combo;
                break;
        }
    }

    return out == expectedval && outcount == sizeof(program);
}

int64_t expected = 0;

void thread_entry(int thread_id) 
{
    int64_t maxval = CASES_PER_THREAD * (thread_id + 1);
    for (int64_t initval = CASES_PER_THREAD * thread_id; initval < maxval; initval++) 
    {
        if (do_simulate(initval, expected)) 
        {
            std::cout << initval << std::endl;
            return;
        }
    }
}

int main() 
{
    
    for (int8_t op : program) 
    {
        expected <<= 3;
        expected |= op;
    }

    // for (int64_t initval = 0; ; initval++) 
    // {
    //     if (initval % 10000 == 0) 
    //     {
    //         std::cout << initval << std::endl;
    //     }

    //     if (do_simulate(initval, expected)) 
    //     {
    //         std::cout << initval << std::endl;
    //         return 0;
    //     }
    // }

    std::thread threads[THREAD_COUNT];

    for (int i = 0; i < THREAD_COUNT; i++) 
    {
        threads[i] = std::thread(thread_entry, i);
    }

    for (int i = 0; i < THREAD_COUNT; i++) 
    {
        threads[i].join();
    }
}