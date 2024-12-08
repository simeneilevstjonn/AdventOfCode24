grid = $<.map{_1.chomp.chars}

an = []

grid.map.with_index{|row,i|
    row.map.with_index{|col,j|
        (-i..(grid.size-1-i)).map{|dy|
            (-j..(grid[0].size-1-j)).map{|dx|
                if dy != 0 || dx != 0
                    found = (-100..100).map{|m|
                        ny = i + m * dy;
                        nx = j + m * dx;
                        ny < grid.size && ny >= 0 && nx < grid[0].size && nx >= 0 && grid[ny][nx] != ?. ? grid[ny][nx] : nil
                    }.compact.tally.any?{_2>1}

                    if found
                        an.push([i,j])
                    end
                end
            }
        }
    }
}

p an.uniq.size
