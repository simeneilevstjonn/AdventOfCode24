grid = $<.map{_1.chomp.chars}

an = []

grid.map.with_index{|row,i|
    row.map.with_index{|col,j|
        (-i/2..(grid.size-1-i)/2).map{|dy|
            (-j/2..(grid[0].size-1-j)/2).map{|dx|
                if dy != 0 || dx != 0
                    if grid[i + dy][j + dx] == grid[i + 2 * dy][j + 2 * dx] && grid[i + dy][j + dx] != ?.
                        an.push([i,j])
                    end
                end
            }
        }
    }
}

p an.uniq.size
