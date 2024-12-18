#include <iostream>
#include <set>
#include <cstring>

static constexpr int GRID_DIM = 71;

bool visited[GRID_DIM][GRID_DIM];
bool blocked[GRID_DIM][GRID_DIM] = { 0 };
// std::set<std::pair<int, int>> blocked = std::set<std::pair<int, int>>();


void dfs(int y, int x) 
{
    visited[y][x] = true;

    if (y > 0) 
    {
        if (!visited[y - 1][x] && !blocked[y - 1][x]) 
        {
            dfs(y - 1, x);
        }
    }
    
    if (x > 0) 
    {
        if (!visited[y][x - 1] && !blocked[y][x - 1]) 
        {
            dfs(y, x - 1);
        }
    }

    if (y < GRID_DIM - 1) 
    {
        std::pair<int, int> p = { y + 1 , x };

        if (!visited[y + 1][x] && !blocked[y + 1][x]) 
        {
            dfs(y + 1, x);
        }
    }

    if (x < GRID_DIM - 1) 
    {
        if (!visited[y][x + 1] && !blocked[y][x + 1]) 
        {
            dfs(y, x + 1);
        }
    }
}

int main() 
{
    
    for (int x, y; ;)
    {
        // std::cin >> x >> y;
        scanf("%d,%d\n", &x, &y);
        std::cout << "Now processing " << x << "," << y << std::endl;

        blocked[y][x] = true;



        memset(visited, 0, sizeof(visited));    

        dfs(0, 0);

        
        // for (int row = 0; row < GRID_DIM; row++) 
        // {
        //     for (int col = 0; col < GRID_DIM; col++) 
        //     {
        //         if (blocked[row][col])
        //         {
        //             std::cout << '#';
        //         }
        //         else if (visited[row][col])
        //         {
        //             std::cout << 'o';
        //         }
        //         else 
        //         {
        //             std::cout << '.';
        //         }
        //     }
        //     std::cout << std::endl;
        // }

        // std::cout << std::endl;

        if (!visited[GRID_DIM - 1][GRID_DIM - 1]) 
        {
            std::cout << "Answer is " << x << "," << y << std::endl;

            for (int row = 0; row < GRID_DIM; row++) 
            {
                for (int col = 0; col < GRID_DIM; col++) 
                {
                    if (blocked[row][col])
                    {
                        std::cout << '#';
                    }
                    else if (visited[row][col])
                    {
                        std::cout << 'o';
                    }
                    else
                    {
                        std::cout << '.';
                    }
                }
                std::cout << std::endl;
            }

            return 0;
        }
    }
}