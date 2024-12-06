g=$<.map{_1.chomp.chars}
def D(y, x, d, grid, stopf)
    while  y >= 0 && x >= 0 && y < grid.size && x < grid[0].size && stopf.(y,x,d) do
        (0..3).map{
            ny,nx=[[y-1,x],[y,x+1],[y+1,x],[y,x-1]][d]
            # puts "attempting transistion from #{[y,x]} to #{[ny, nx]}"
            if ny >= 0 && nx >= 0 && ny < grid.size && nx < grid[0].size && grid[ny][nx] == ?#
                d += 1
                d %= 4
                # puts "hit target, turning right"
            else
                y,x=ny,nx
                break
            end
        }
    end
end
t=[]
D(*g.map.with_index{[_2,_1.index(?^)]}.find{_2},0,g,->(y,x,d){t.push([y,x,d]);true})
p (1...t.size).map{|i|y,x,d=t[i];g[y][x]=?#;l=0;v=g.map{_1.map{[false]*4}};D(*t[0],g,->(y,x,d){v[y][x][d]?(l=1;false):(v[y][x][d]=true)});g[y][x]=?.;l>0?[y,x]:0}.uniq.size-1