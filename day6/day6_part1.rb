grid = $<.map{_1.chomp.chars}

y, x = grid.map.with_index{[_2,_1.index(?^)]}.find{_2}
p [y,x]
d = 0
while  y >= 0 && x >= 0 && y < grid.size && x < grid[0].size do
    grid[y][x] = ?X
    (0..3).map{
        ny,nx=[[y-1,x],[y,x+1],[y+1,x],[y,x-1]][d]
        puts "attempting transistion from #{[y,x]} to #{[ny, nx]}"
        if ny >= 0 && nx >= 0 && ny < grid.size && nx < grid[0].size && grid[ny][nx] == ?#
            d += 1
            d %= 4
            puts "hit target, turning right"
        else
            y,x=ny,nx
            break
        end
    }
end

# grid.map{puts _1.join}

p grid.sum{_1.count ?X}
