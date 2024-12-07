#include <iostream>
#include <thread>
#include <string>
#include <sstream>

static constexpr int THREAD_COUNT = 16;
static constexpr size_t MAX_NUMS_PER_ROW = 100;
static constexpr size_t MAX_CASES = 1000;

struct AoCCase 
{
    long long sum;
    int number_count;
    int numbers[MAX_NUMS_PER_ROW];
};

long long powi(long long base, unsigned int exp)
{
    long long res = 1;
    while (exp) {
        if (exp & 1)
            res *= base;
        exp >>= 1;
        base *= base;
    }
    return res;
}

long long concat(long long left, long long right) 
{
    long long factor = 1;
    for (; right / factor; factor *= 10);

    return left * factor + right;
}

class AoCSolver 
{
public:
    AoCCase* TestCases;
    int testcase_count;

    long long answer;

    long long solve_testcase(AoCCase acase) 
    {

        const long long max_val = powi(3, acase.number_count - 1);
        
        for (long long i = 0; i < max_val; i++) 
        {
            long long result = acase.numbers[0];

            long long comb = i;

            for (int j = 1; j < acase.number_count; j++) 
            {
                switch (comb % 3) 
                {
                    case 0:
                        result += acase.numbers[j];
                        break;
                    case 1:
                        result *= acase.numbers[j];
                        break;
                    case 2:
                        result = concat(result, acase.numbers[j]);
                    break;
                }

                if (result > acase.sum) 
                {
                    break;
                }
            }

            if (result == acase.sum) 
            {
                return result;
            }
        }

        return 0;
    }

    void solve() 
    {
        answer = 0;

        for (int i = 0; i < testcase_count; i++) 
        {
            answer += solve_testcase(TestCases[i]);
        }
    }

};

static AoCSolver solvers[THREAD_COUNT];

static void thread_entry(int solverid) 
{
    solvers[solverid].solve();
}

int main() 
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    AoCCase cases[MAX_CASES];

    int case_count = 0;

    for (std::string line; std::getline(std::cin, line); case_count++)
    {
        cases[case_count] = { 0 };
        std::istringstream stream(line);
        stream >> cases[case_count].sum;
        char c;
        stream >> c;

        for (; (stream >> cases[case_count].numbers[cases[case_count].number_count]); cases[case_count].number_count++) 
        {
            
        }
    }


    std::thread threads[THREAD_COUNT];

    const int PER_THREAD = case_count / THREAD_COUNT;

    for (int i = 0; i < THREAD_COUNT; i++) 
    {
        solvers[i].TestCases = cases + (i * PER_THREAD);
        solvers[i].testcase_count = PER_THREAD;

        if (i == THREAD_COUNT - 1) 
        {
            solvers[i].testcase_count += case_count - THREAD_COUNT * PER_THREAD;
        }

        threads[i] = std::thread(thread_entry, i);
    }

    for (int i = 0; i < THREAD_COUNT; i++) 
    {
        threads[i].join();
    }

    long long res = 0;

    for (int i = 0; i < THREAD_COUNT; i++) 
    {
        res += solvers[i].answer;
    }

    std::cout << res << std::endl;
}